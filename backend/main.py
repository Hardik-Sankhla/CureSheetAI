# backend/main.py

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import re
import logging

app = FastAPI(
    title="🧠 MedNote Structurer API",
    description="Extracts structured data from clinical notes using LLaMA2 or LLaMA3",
    version="1.0.0"
)

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

def query_llama(prompt: str) -> dict:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=300
        )
        response.raise_for_status()
        raw = response.json()["response"].strip()

        # Extract JSON using regex (in case the model wraps it with text)
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            logging.warning("No valid JSON found in LLaMA response")
            return {
                "symptoms": "N/A",
                "diagnosis": "N/A",
                "medications": "N/A",
                "follow_up": "N/A"
            }
    except Exception as e:
        logging.error(f"LLaMA3 API error: {e}")
        return {
            "symptoms": "N/A",
            "diagnosis": "N/A",
            "medications": "N/A",
            "follow_up": "N/A"
        }

@app.post("/extract/")
def extract_medical_info(note: str = Form(...)) -> dict:
    prompt = (
        "Extract the following from the doctor's note:\n"
        "- Symptoms\n- Diagnosis\n- Medications\n- Follow-up Instructions\n"
        "Return the output in JSON format with keys: symptoms, diagnosis, medications, follow_up.\n\n"
        f"Note:\n{note}"
    )
    structured_data = query_llama(prompt)
    return structured_data
