from crewai import Agent
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)


class Agents:
    def job_researcher(self):
        return Agent(
            role="Job Researcher",
            goal="Make sure to do amazing analysis on "
                "job posting to help job applicants",
            verbose=True,
            #tools=[SerperDevTool(n_results=5), ScrapeWebsiteTool()],
            tools=[ SerperDevTool(), ScrapeWebsiteTool()],
            backstory=(
                "As a Job Researcher, your prowess in "
                "navigating and extracting critical "
                "information from job postings is unmatched."
                "Your skills help pinpoint the necessary "
                "qualifications and skills sought "
                "by employers, forming the foundation for "
                "effective application tailoring."
            )
        )
        
    def profile_builder(self):
        return Agent(
            role="Profile Builder",
            goal="Do incredible research on job applicants"
                "to help them stand out in the job market",
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool(), FileReadTool(file_path='/tmp/cv.md'),MDXSearchTool(mdx='/tmp/cv.md')],
            backstory=(
                "Equipped with analytical prowess, you dissect "
                "and synthesize information "
                "from diverse sources to craft comprehensive "
                "personal and professional profiles, laying the "
                "groundwork for personalized resume enhancements."
            )
        )

    def resume_strategist(self):
        return Agent(
            role="Resume Strategist",
            goal="Find all the best ways to make a "
                 "resume stand out in the job market.",
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool(), FileReadTool(file_path='/tmp/cv.md'),MDXSearchTool(mdx='/tmp/cv.md')],
            backstory=(
                "With a strategic mind and an eye for detail, you "
                "excel at refining resumes to highlight the most "
                "relevant skills and experiences, ensuring they "
                "resonate perfectly with the job's requirements."
            )
        )
        
    def interview_preparer(self):
        return Agent(
            role="Interview Preparer",
            goal="Create interview questions and talking points "
                    "based on the resume and job requirements",
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool(), FileReadTool(file_path='/tmp/cv.md'),MDXSearchTool(mdx='/tmp/cv.md')],
            backstory=(
                "Your role is crucial in anticipating the dynamics of "
                "interviews. With your ability to formulate key questions "
                "and talking points, you prepare candidates for success, "
                "ensuring they can confidently address all aspects of the "
                "job they are applying for."
            )
        )