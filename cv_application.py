from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)
from crewai import Crew
from tasks import Tasks
from agents import Agents
import os

class CVApplication:
    def __init__(self, serper_api_key, openai_api_key):
        self.serper_api_key = serper_api_key
        self.openai_api_key = openai_api_key
        self.tasks = Tasks()
        self.agents = Agents()
        self.cvapplication_crew = Crew(
            agents=[
                self.agents.job_researcher(),
                self.agents.profile_builder(),
                self.agents.resume_strategist(),
                self.agents.interview_preparer()
            ],
            tasks=[
                self.tasks.research_task(),
                self.tasks.profile_task(),
                self.tasks.resume_task(),
                self.tasks.interview_task()
            ]
            ,verbose=True
        )
        
    def cv_application(self, job_search):
        result = self.cvapplication_crew.kickoff(inputs={"job_search": job_search})
        
        if result:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            file_path = os.path.join(script_dir, "tailored_resume.md")
            
            with open(file_path, "r") as f:
                tailored_resume = f.read()
            return tailored_resume
        else:
            return None
