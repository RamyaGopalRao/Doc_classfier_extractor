import gradio as gr
import asyncio
from runner_file import run_document_pipeline

def run_pipeline_sync(files):
    return asyncio.run(run_document_pipeline(files))

gr.Interface(
    fn=run_pipeline_sync,
    inputs=gr.File(file_types=[".jpg", ".png", ".pdf"], file_count="multiple", label="Upload Documents"),
    outputs="text",
    title="🧠 Agentic Document Verifier",
    description="Upload PAN, Aadhaar, Tax, or License documents. The system will classify, extract, verify, and generate a report."
).launch()

