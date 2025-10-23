from agents import Agent
from pydantic import BaseModel

class ClassificationRequest(BaseModel):
    ocr_text: str

class ClassificationResponse(BaseModel):
    document_type: str

classifier_agent = Agent(
    name="ClassifierAgent",
    instructions="Classify the document as one of: PAN, AADHAAR, DRIVING_LICENSE, TAX.",
    model="gpt-4o",
    output_type=ClassificationResponse
)
