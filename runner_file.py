import os
from agents import Runner
from docai_agents.ocr_agent import ocr_agent,OCRResponse
from docai_agents.classfiier_agent import classifier_agent
from docai_agents.extractor_agent import extractor_agent
from docai_agents.verifier_agent import verifier_agent
from docai_agents.report_agent import report_agent
from utils import encode_image_to_base64
from dotenv import load_dotenv

load_dotenv(override=True)

# Verify API key is loaded
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("⚠️ WARNING: OPENAI_API_KEY not found in environment variables!")
else:
    print("✅ OPENAI_API_KEY loaded successfully")

async def run_document_pipeline(files):
    verified_data = {}

    for file in files:
        base64_img = encode_image_to_base64(file)
        print(base64_img)
        data_uri = f"data:image/jpeg;base64,{base64_img}"
        
        # The prompt uses the Data URI
        ocr_prompt = f"Please extract all readable text from this image: {data_uri}"
        
        ocr_result = await Runner.run(ocr_agent, ocr_prompt)
        # ... (Rest of the OCR output handling logic) ...
        
        # Assuming OCRResponse is imported and correctly used:
        if isinstance(ocr_result.final_output, OCRResponse):
            ocr_text = ocr_result.final_output.extracted_text
        else:
            # Add robust error handling here if the agent fails structure
            print("❌ OCR Agent did not return the expected structured output.")
            ocr_text = ""

        # ocr_result = await Runner.run(ocr_agent, {"image_base64": base64_img})
        # ocr_text = ocr_result.final_output
        # print(ocr_text)

        classify_result = await Runner.run(classifier_agent, f"OCR Text:\n{ocr_text}")
        doc_type = classify_result.final_output

        extract_result = await Runner.run(extractor_agent, f"Document Type: {doc_type}\n\nOCR Text:\n{ocr_text}")
        extracted_fields = extract_result.final_output

        verify_result = await Runner.run(verifier_agent, f"Document Type: {doc_type}\n\nExtracted Fields:\n{extracted_fields}")
        verified_data[doc_type] = verify_result.final_output

    report_result = await Runner.run(report_agent, f"Verified Data:\n{verified_data}")
    return report_result.final_output
