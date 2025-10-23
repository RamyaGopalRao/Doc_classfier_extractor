from agents import Agent
from pydantic import BaseModel
from typing import Dict, Any

class ExtractionRequest(BaseModel):
    document_type: str
    ocr_text: str

class ExtractionResponse(BaseModel):
    fields: Dict[str, Any]

extractor_agent = Agent(
    name="ExtractorAgent",
    instructions="Extract relevant fields from the OCR text based on the document type. Return JSON.",
    model="gpt-4o",
    output_type=ExtractionResponse
)
