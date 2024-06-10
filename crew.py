from crewai import Crew
from textwrap import dedent

from dotenv import load_dotenv
load_dotenv()

from Tasks import JJMTasks
from Agents import JJMAgents

class JJMCrew():

    def __init__(self,query):
        self.query = query

    def run(self):

        agents = JJMAgents()
        tasks = JJMTasks()

        admin = agents.AdminAgent()
        task = tasks.AnswerTheQuery(self.query)

        crew = Crew(
            agents=[admin], tasks=[task],verbose=True
        )

        result = crew.kickoff()
        return result