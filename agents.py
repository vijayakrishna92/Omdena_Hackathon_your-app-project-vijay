# agents.py

from crewai import Agent
from langchain.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv
from web_scraper import search_and_scrape
from langchain_groq import ChatGroq
load_dotenv()

HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
#mistral = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768",api_key=os.getenv('GROQ_API_KEY'))
mistral = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.3, huggingfacehub_api_token=HUGGINGFACE_API_KEY)


class Agents:
    def agenter(self, topic): 
        return Agent(
            role="Fake News Detector",  # Define the role of the agent
            goal=f"Determine if the statement '{topic}' is genuine or fake based on web searches and analysis.",
            backstory=f"""
                The agent is designed to analyze claims and verify them using the latest web search tools.
                It assesses the credibility of information and compares it with known sources.
            """,
            llm=mistral,
            tools = [search_and_scrape],
            allow_delegation=False,
            verbose=True
        )