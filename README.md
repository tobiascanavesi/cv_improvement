# CV Improvement App

## Overview

The CV Improvement App is a Streamlit application designed to help users enhance their CVs for specific job searches. By leveraging AI agents, the app analyzes job postings and personal CVs, tailoring them to better match job requirements. The app supports both Markdown and PDF CV formats, with PDF parsing powered by the LlamaParse library.

## Features

- **Job Search Integration:** Paste the job search description and let the app tailor your CV accordingly.
- **CV Upload:** Upload your CV in Markdown or PDF format. PDFs require a LLAMA_CLOUD_API_KEY for conversion.
- **Interview Material:** Optionally receive tailored interview materials based on your CV and job description.
- **Downloadable Results:** Get your tailored CV and interview materials as downloadable Markdown files.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/tobiascanavesi/cv_improvement.git
    cd cv-improvement-app
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file and add your API keys:**
    ```
    SERPER_API_KEY=your_api_key_here
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run streamlit_app.py
    ```

2. **Upload your CV and enter the job description in the provided fields.**

3. **Click "Submit" to get a tailored CV.**

## Agents

The app uses four specialized AI agents to provide a comprehensive CV enhancement experience:

1. **Job Researcher**
   - **Role:** Analyzes job postings.
   - **Goal:** Extracts critical information from job postings to help tailor applications.
   - **Tools:** SerperDevTool, ScrapeWebsiteTool.

2. **Profile Builder**
   - **Role:** Builds detailed profiles of job applicants.
   - **Goal:** Enhances personal and professional profiles for better job market positioning.
   - **Tools:** SerperDevTool, ScrapeWebsiteTool, FileReadTool, MDXSearchTool.

3. **Resume Strategist**
   - **Role:** Refines resumes to highlight key skills and experiences.
   - **Goal:** Makes resumes stand out by aligning them with job requirements.
   - **Tools:** SerperDevTool, ScrapeWebsiteTool, FileReadTool, MDXSearchTool.

4. **Interview Preparer**
   - **Role:** Prepares interview questions and talking points.
   - **Goal:** Ensures candidates are well-prepared for interviews.
   - **Tools:** SerperDevTool, ScrapeWebsiteTool, FileReadTool, MDXSearchTool.

## Flow Diagram

![Agent Flow Diagram](/img/cv_improvement.png)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

If you like you can follow me at [LinkedIn](https://www.linkedin.com/in/tcanavesi/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.