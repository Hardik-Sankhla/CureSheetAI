# frontend/app.py

import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(page_title="🏥 MedNote Structurer Pro", layout="wide")

st.markdown("""
    <style>
        .title { font-size: 2.5rem; font-weight: 700; color: #4a0b8c; }
        .subtext { font-size: 1.1rem; color: gray; }
        .stDownloadButton > button { background-color: #4a0b8c; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🏥 MedNote Structurer Pro</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Upload clinical notes and extract structured data (Symptoms, Diagnosis, Medications, Follow-up).</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload clinical notes CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.info(f"✅ Uploaded {len(df)} clinical notes.")
    results = []

    with st.spinner("🧠 Extracting structured data using LLaMA model..."):
        for idx, row in df.iterrows():
            patient_id = row.get("patient_id", idx + 1)
            note = row.get("doctor_notes", "")
            st.write(f"🧠 Processing note {idx+1} of {len(df)} (Patient ID: {patient_id})...")

            try:
                response = requests.post(
                    "http://localhost:8000/extract/",
                    data={"note": note},  # using `data` to send as Form (not JSON)
                    timeout=120
                )
                response.raise_for_status()
                structured = response.json()
            except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                st.error(f"❌ Error processing note for patient {patient_id}: {e}")
                structured = {
                    "symptoms": "N/A",
                    "diagnosis": "N/A",
                    "medications": "N/A",
                    "follow_up": "N/A"
                }

            results.append({
                "patient_id": patient_id,
                "doctor_notes": note,
                **structured
            })

    result_df = pd.DataFrame(results)
    st.success("✅ Extraction complete!")

    st.markdown("### 🗂️ Structured Clinical Data")
    st.dataframe(result_df, use_container_width=True)

    st.download_button(
        label="📥 Download Structured Notes",
        data=result_df.to_csv(index=False),
        file_name="structured_notes.csv",
        mime="text/csv"
    )
