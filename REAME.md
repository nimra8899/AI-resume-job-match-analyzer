# AI Resume & Job Match Analyzer

An AI-powered web application that compares a candidate's resume with a job description and identifies matching skills, skill gaps, strengths, and areas for improvement.

## Features

- Upload resumes in PDF format
- Extract resume text using PyPDF
- Analyze resumes against job descriptions
- Generate an AI-estimated match score
- Identify matched and missing skills
- Provide personalized resume improvement suggestions
- Return structured analysis using Pydantic
- Download the analysis report

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM:** Google Gemini API
- **PDF Processing:** pypdf
- **Data Validation:** Pydantic
- **Environment Variables:** python-dotenv
- **Version Control:** Git and GitHub

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-resume-job-match-analyzer.git
   cd ai-resume-job-match-analyzer
   ```

2. Create and activate a virtual environment.

   Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

   Replace the placeholder with your own Gemini API key. Never commit this file.

5. Run the application:

   ```bash
   streamlit run app.py
   ```

## How It Works

1. The user uploads a PDF resume.
2. The application extracts its text.
3. The user provides a job description.
4. The Gemini API analyzes the resume against the job requirements.
5. The application validates and displays the structured results.

## Limitations

The match score is an AI-generated estimate, not an official ATS score or a prediction of hiring success. Results depend on the resume text, job description, model output, and available API quota.

## Security and Privacy

Do not commit API keys, personal resumes, or other confidential information. Review third-party API privacy terms before submitting sensitive documents.

## Future Improvements

- Semantic similarity using text embeddings
- Retrieval-Augmented Generation (RAG)
- Support for scanned PDFs through OCR
- FastAPI backend
- Deployment and automated testing