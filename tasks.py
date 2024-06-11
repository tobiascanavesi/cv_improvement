from crewai import Task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, FileReadTool
from agents import Agents

class Tasks:
    def __init__(self):
        self.agents = Agents()

    def research_task(self):
        return Task(
            description=("Analyze the job posting URL provided ({job_search}) "
                    "to extract key skills, experiences, and qualifications "
                    "required. Use the tools to gather content and identify "
                    "and categorize the requirements."),
            expected_output=("A structured list of job requirements, including necessary"
                            "skills, qualifications, and experiences."),
            tools=[],
            agent = self.agents.job_researcher(),
            #async_execution = True
        )
    def profile_task(self):
        return Task(
            description=("Analyze the CV provided to extract key skills, experiences, "
                    "and qualifications. Use the tools to gather content and identify "
                    "and categorize the information."),
            expected_output=("A structured list of skills, qualifications, and experiences "
                            "from the CV."),
            tools=[FileReadTool(file_path='/tmp/cv.md')],
            agent = self.agents.profile_builder(),
            #async_execution = True
        )
        
        
    def resume_task(self):
        return Task(
            description=("Using the profile and job requirements obtained from "
                "previous tasks, tailor the resume to highlight the most "
                "relevant areas. Employ tools to adjust and enhance the "
                "resume content. Make sure this is the best resume even but "
                "don't make up any information. Update every section, "
                "inlcuding the initial summary, work experience, skills, "
                "and education. All to better reflrect the candidates "
                "abilities and how it matches the job posting."),
            expected_output=("An updated resume that effectively highlights the candidate's "
                             "qualifications and experiences relevant to the job."),
            output_file="tailored_resume.md",
            context=[self.research_task(), self.profile_task()],
            agent = self.agents.resume_strategist()
        )
        
    def interview_task(self):
        return Task(
            description=("Create a set of potential interview questions and talking "
                "points based on the tailored resume and job requirements. "
                "Utilize tools to generate relevant questions and discussion "
                "points. Make sure to use these question and talking points to "
                "help the candiadte highlight the main points of the resume "
                "and how it matches the job posting."),
            expected_output=("A document containing key questions and talking points "
                        "that the candidate should prepare for the initial interview."),
            tools=[],
            context=[self.research_task(), self.profile_task(), self.resume_task()],
            output_file="interview_materials.md",
            agent = self.agents.interview_preparer()
        )