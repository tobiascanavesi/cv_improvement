from dotenv import load_dotenv
import streamlit as st
from cv_application import CVApplication


load_dotenv()
# This app will pick in a cv in a markdown format and adjusted for adequate to a linkedin search.

def main():
    st.title("CV Improvement")
    st.write("This app will help you improve your CV for a particular job search.")
    
    job_search = st.text_area("Paste the job search here:").strip()
    job_search_string = f'"{job_search}"'
    uploaded_file = st.file_uploader("Upload your CV in markdown format", type=["md"])
    
    # Show also the the inverview material
    interview_material = st.checkbox("Show Interview Material")
    
    if uploaded_file is not None:
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
        st.warning("Please upload your CV in markdown format.")
                
if __name__ == "__main__":
    main()