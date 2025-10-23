from agents import Agent
from pydantic import BaseModel
from typing import Dict

class ReportRequest(BaseModel):
    verified_data: Dict[str, Dict[str, float]]

class ReportResponse(BaseModel):
    report_text: str

report_agent = Agent(
    name="ReportAgent",
    instructions="Generate a readable report from the verified document data.",
    model="gpt-4o",
    output_type=ReportResponse
)
