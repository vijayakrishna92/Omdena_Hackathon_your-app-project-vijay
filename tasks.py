# tasks.py

from crewai import Task
from textwrap import dedent


class Tasks:
    def tasker(self, agent, topic): 
        return Task(
            description=dedent(f"""
                1. Conduct a web search for the topic '{topic}' to find relevant articles.
                2. Analyze the retrieved articles for credibility and fact-checking.
                3. Provide a conclusion on whether the statement is genuine or fake.
            """),
            expected_output=dedent(f"""
                The analysis will output either 'Genuine' or 'Fake' based on the information retrieved.
            """),
            agent=agent
        )