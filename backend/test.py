from fastapi import FastAPI, Form
import requests

app = FastAPI()

def query_llama(prompt: str) -> str:
    """
    Sends a prompt to the Llama3 model running on localhost:11434 and returns the response.

    Args:
        prompt (str): The text prompt to send to the Llama3 model.

    Returns:
        str: The stripped response from the Llama3 model.
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=300  # Increased timeout for longer processing time
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Llama3 API. Is it running on http://localhost:11434?")
        return "Error: Llama3 API not reachable."
    except requests.exceptions.Timeout:
        print("Error: The request to Llama3 API timed out.")
        return "Error: Llama3 API response timed out."
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred during the request: {e}")
        return f"Error: An unexpected API error occurred: {e}"
    except KeyError:
        print("Error: 'response' key not found in Llama3 API's JSON response.")
        return "Error: Unexpected response format from Llama3 API."


@app.post("/extract/")
def extract_medical_info(note: str = Form(...)) -> dict:
    """
    Extract medical information from a doctor's note using the Llama3 model.

    Args:
        note (str): The doctor's note to extract information from.

    Returns:
        dict: Extracted structured medical data as JSON.
    """
    prompt = (
        "Extract the following from the doctor's note:\n"
        "- Symptoms\n- Diagnosis\n- Medications\n- Follow-up Instructions\n"
        "Return the output in JSON format.\n\n"
        f"Note:\n{note}"
    )
    structured_data = query_llama(prompt)
    return {"structured": structured_data}
