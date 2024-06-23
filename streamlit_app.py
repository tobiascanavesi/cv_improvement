import os
import streamlit as st
from dotenv import load_dotenv
from cv_application import CVApplication
from llama_parse import LlamaParse

# Load environment variables from .env file
load_dotenv()

# Define the main function for the Streamlit app
def main():
    st.title("CV Improvement")
    st.write("This app will help you improve your CV for a particular job search.")
    #Write in bold that when the file is a pdf you will need to enter the api key, from llama cloud
    st.markdown("**Note:** If you upload a PDF file, you will need to enter your LLAMA_CLOUD_API_KEY.")
    
    job_search = st.text_area("Paste the job search here:").strip()
    job_search_string = f'"{job_search}"'
    
    # Add a file uploader that accepts both markdown and PDF files
    uploaded_file = st.file_uploader("Upload your CV (markdown or PDF)", type=["md", "pdf"])
    
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
                cv_application = CVApplication()
                
                tailored_resume = cv_application.cv_application(job_search_string)
                if tailored_resume:
                    st.success("CV analysis completed!")
                    st.markdown("### Tailored Resume")
                    st.markdown(tailored_resume)
                    
                    if interview_material:
                        interview_material_path = "interview_materials.md"
                        with open(interview_material_path, "r") as f:
                            interview_material = f.read()
                        st.markdown("### Interview Material")
                        st.markdown(interview_material)
                else:
                    st.error("An error occurred during CV analysis.")
    else:
        st.warning("Please upload your CV (markdown or PDF).")
                
if __name__ == "__main__":
    main()
