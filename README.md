<h1 align="center">✨ CureSheet AI</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/Hardik-Sankhla/CureSheetAI/main/Image/CureSheetBanner.png">
</p>

## 🎯**CureSheet AI**  

___

### **Introduction:**  

The **CureSheet AI - Medical Note Structurer** is an AI-powered tool designed to convert unstructured clinical notes into structured data, enhancing efficiency and accuracy in healthcare documentation. By leveraging advanced natural language processing models, this tool helps healthcare professionals efficiently parse and organize patient information to improve decision-making and record-keeping.

___

## 🎯 What is CureSheet AI?

**CureSheet AI** is an innovative solution tailored for healthcare providers who handle a large volume of clinical notes. This tool is particularly beneficial for clinics and hospitals, which deal with numerous patient records daily. The structurer employs state-of-the-art language models, such as LLaMA2 hosted via Ollama, to extract key information like symptoms, diagnosis, medications, and follow-up instructions.

___

## 🔥 Core Features

- 🩺 **Symptom Extraction** – Identifies and extracts symptoms mentioned in the clinical notes.
- 🧾 **Diagnosis Detection** – Extracts the diagnosis provided by the healthcare professional.
- 💊 **Medication Identification** – Lists medications prescribed in the notes.
- 📅 **Follow-up Instructions** – Extracts any follow-up instructions given to the patient.
- 📈 **Interactive Dashboard** – Built with Streamlit, the dashboard allows users to upload CSV files of clinical notes and view structured data.
- 📥 **Downloadable Data** – Users can download the structured data as a CSV file for integration with EMR systems.
- ⚙️ **Technical Stack** – Backend developed using FastAPI, frontend with Streamlit, and data manipulation with Pandas.
- 🚀 **Deployment Ready** – Containerized using Docker for consistent deployment environments and suitable for cloud deployment on platforms like AWS, Azure, or Heroku.

___

## Project Structure and Organization

    curesheet-ai/
    ├── backend/
    │   ├── main.py
    │   ├── utils.py
    │   ├── models/
    │   └── tests/
    ├── frontend/
    │   ├── app.py
    │   └── components/
    ├── data/
    │   └── example_notes.csv
    ├── docker/
    │   ├── Dockerfile
    │   └── docker-compose.yml
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── requirements.txt
    ├── README.md
    └── LICENSE

___

## 🛠️ Installation

1. **Clone the Repository:**

   ```python
   $ git clone https://github.com/yourusername/curesheet-ai.git
   $ cd curesheet-ai
    ```

2. **Set Up a Virtual Environment:**

    ```python
    $ python -m venv venv
    $ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```python
    $ pip install -r requirements.txt
    ```

4. **Run the Backend:**

    ```python
    $ uvicorn backend.main:app --reload
    ```

5. **Run the Frontend:**

    ```python
    $ streamlit run frontend/app.py
    ```
___

## 🚀 UsageUpload CSV:

- Use the dashboard to upload a CSV file containing clinical notes.
- Analyze Notes: The tool will process the notes and display structured data including symptoms, diagnosis, medications, and follow-up instructions.- - - - Download Results: Download the structured data as a CSV file for further use.

![Usage](https://raw.githubusercontent.com/Hardik-Sankhla/CureSheetAI/main/Image/Usage.png)
___

## Results: 

| ![Integration 1](https://raw.githubusercontent.com/Hardik-Sankhla/CureSheetAI/main/Image/Result1.png) |
|:---:|
| ![Integration 2](https://raw.githubusercontent.com/Hardik-Sankhla/CureSheetAI/main/Image/Result2.png) |

___

## 🤝 Contribution

We welcome contributions to enhance CureSheet AI!

- Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

 For any inquiries or feedback, please contact [Hardik Sankhla](https://github.com/Hardik-Sankhla). 

