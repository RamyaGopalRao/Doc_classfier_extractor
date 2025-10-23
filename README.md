# 🧠 Document Classifier & Extractor using OpenAI SDK + Gradio

## 📌 Overview
This project is an interactive document intelligence tool that classifies uploaded documents and extracts structured information using OpenAI's GPT models. It features a Gradio-powered UI for seamless user interaction and leverages prompt engineering for zero-shot classification and semantic extraction.

## 🚀 Features
- **Document Classification**: Automatically identifies document types (e.g., resume, invoice, ID proof) using GPT-based semantic understanding.
- **Information Extraction**: Extracts key fields like name, date, ID number, or skills using prompt-driven GPT calls.
- **Gradio Interface**: Drag-and-drop UI for uploading PDFs or images, with real-time display of extracted data.
- **Multi-format Support**: Handles scanned PDFs, digital documents, and images with OCR fallback.
- **Modular Agent Design**: Built with extensible agent abstractions for classification, extraction, and verification stages.
- **OpenAI SDK Integration**: Uses `openai.ChatCompletion` for prompt-based logic.

## 🧰 Tech Stack
- Python
- OpenAI SDK
- Gradio
- PyMuPDF, pdfplumber (PDF parsing)
- Pydantic (data validation)
- Optional: OpenAI
## 📦 Installation
```bash
git clone https://github.com/RamyaGopalRao/doc_classifier_extractor.git
cd doc_classifier_extractor
pip install -r requirements.txt
python main.py
