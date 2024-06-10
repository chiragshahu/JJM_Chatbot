from crewai import Task
from textwrap import dedent
from Agents import JJMAgents

from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model="llama3-70b-8192")

class JJMTasks():

    def AnswerTheQuery(self,question):

        agents = JJMAgents()
        admin_agent = agents.AdminAgent()

        task = Task(
            description=f"""Provide answer of the question : {question}\n
            Provide short answer in english, simple so a normal citizen can understand.
            """,
            expected_output="A chat like answer to the question",
            agent=admin_agent
        )
        return task