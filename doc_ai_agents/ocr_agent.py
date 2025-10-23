from agents import Agent
from pydantic import BaseModel

class OCRRequest(BaseModel):
    image_base64: str

class OCRResponse(BaseModel):
    extracted_text: str

ocr_agent = Agent(
    name="OCRAgent",
    instructions="Extract all readable text from the image. Return only the raw text.",
    model="gpt-4-turbo",
    
)
