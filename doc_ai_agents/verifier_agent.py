from agents import Agent
from pydantic import BaseModel
from typing import Dict

class VerificationRequest(BaseModel):
    document_type: str
    extracted_fields: Dict[str, str]

class VerificationResponse(BaseModel):
    verified_fields: Dict[str, float]

verifier_agent = Agent(
    name="VerifierAgent",
    instructions="Return confidence scores (0 to 1) for each extracted field.",
    model="gpt-4o",
    output_type=VerificationResponse
)
