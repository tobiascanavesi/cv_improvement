import os
import streamlit as st
from dotenv import load_dotenv
from cv_application import CVApplication
from llama_parse import LlamaParse

# Load environment variables from .env file
load_dotenv()

# Define the main function for the Streamlit app
def main():
    st.set_page_config(page_title="CV Improvement", layout="wide")
    
    # Add the logo
    logo_path = "logo.png"
    st.image(logo_path, width=100)
    
    # Custom CSS for labels
    st.markdown(
        """
        <style>
        .custom-label {
            font-size: 1rem; 
            font-weight: Semi Bold;
        }
        .hidden-label {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Centered title and description
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>CV Improvement</h1>
            <p class="custom-label">This app will help you improve your CV for a particular job search.</p>
            <p style="color: yellow;">Note: If you upload a PDF file, you will need to enter your LLAMA_CLOUD_API_KEY.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Prompt user to enter API keys
    serper_api_key = st.text_input("Enter your SERPER_API_KEY", type="password")
    openai_api_key = st.text_input("Enter your OPENAI_API_KEY", type="password")
    
    if not serper_api_key or not openai_api_key:
        st.warning("Please enter both your SERPER_API_KEY and OPENAI_API_KEY.")
        return
    
    # Custom HTML for the labels
    st.markdown('<p class="custom-label">Paste the job search here:</p>', unsafe_allow_html=True)
    job_search = st.text_area("Enter job search", placeholder="Enter job description", label_visibility="collapsed").strip()
    job_search_string = f'"{job_search}"'
    
    st.markdown('<p class="custom-label">Upload your CV (Markdown or PDF):</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload CV", type=["md", "pdf"], label_visibility="collapsed")
    
    interview_material = st.checkbox("Show Interview Material")
    
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            # Prompt the user to enter their LLAMA_CLOUD_API_KEY
            api_key = st.text_input("Enter your LLAMA_CLOUD_API_KEY", type="password")
            
            if api_key:
                # Save the PDF to a temporary location
                pdf_path = f"/tmp/{uploaded_file.name}"
                with open(pdf_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Convert the PDF to markdown using the LlamaParse library
                document = LlamaParse(result_type="markdown", api_key=api_key).load_data(pdf_path)
                file_name = "cv.md"
                text_path = f"/tmp/{file_name}"
                with open(text_path, 'w') as file:
                    file.write(document[0].text)
            else:
                st.warning("Please enter your LLAMA_CLOUD_API_KEY.")
                return
        else:
            # If the file is a markdown file, save it directly
            uploaded_file.name = "cv.md"
            text_path = f"/tmp/{uploaded_file.name}"
            with open(text_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        
        submit_button = st.button("Submit")
        
        if submit_button:
            with st.spinner("Analyzing your CV..."):
                cv_application = CVApplication(serper_api_key=serper_api_key, openai_api_key=openai_api_key)
                
                tailored_resume = cv_application.cv_application(job_search_string)
                if tailored_resume:
                    st.success("CV analysis completed!")
                    st.markdown("### Tailored Resume")
                    st.markdown(tailored_resume)
                    
                    # Download button for tailored resume
                    st.download_button(
                        label="Download Tailored Resume",
                        data=tailored_resume,
                        file_name="tailored_resume.md",
                        mime="text/markdown"
                    )
                    
                    if interview_material:
                        interview_material_path = "interview_materials.md"
                        with open(interview_material_path, "r") as f:
                            interview_material_content = f.read()
                        st.markdown("### Interview Material")
                        st.markdown(interview_material_content)
                        
                        # Download button for interview material
                        st.download_button(
                            label="Download Interview Material",
                            data=interview_material_content,
                            file_name="interview_material.md",
                            mime="text/markdown"
                        )
                else:
                    st.error("An error occurred during CV analysis.")
    else:
        st.warning("Please upload your CV (Markdown or PDF).")

if __name__ == "__main__":
    main()
