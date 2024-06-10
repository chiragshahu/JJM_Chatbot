from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools.search_tools import SerachTools
from tools.rag_tool import RAGTool

llm = ChatGroq(model="llama3-70b-8192")

class JJMAgents():


    def AdminAgent(self):
        Admin = Agent(
            role = "Jal Jeevan Mission Assistant",
            goal = "Providing accurate infirmation related to Jal Jeevan Mission.",
            backstory = """You are appointed by government of india to assist team 
            working on making tape water available to the last rural area of the 
            country""",
            verbose=True,
            function_calling_llm=llm,
            allow_delegation=True,
            tools=[SerachTools.search_internet, RAGTool.rag_search_tool])
        
        return Admin
