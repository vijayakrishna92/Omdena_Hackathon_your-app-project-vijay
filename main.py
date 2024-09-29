#main.py
import streamlit as st
from crewai import Crew
from agents import Agents
from tasks import Tasks


class ContentCrew:
    def __init__(self, topic):
        self.topic = topic
        
    def run(self):
        agents = Agents()  # Ensure this is correctly instantiated
        tasks = Tasks()
        agenter = agents.agenter(self.topic)
        
        tasker = tasks.tasker(agenter, self.topic)
        
        crew_1 = Crew(
            agents=[agenter],
            tasks=[tasker],
            verbose=True
        )
        
        result_1 = crew_1.kickoff()  # Start the crew operation
        st.write(result_1)

# Streamlit UI
st.title('Fake News Detection Tool')
st.write('-------------------------------')
topic = st.text_input("Enter a statement to verify:")
if st.button('Verify'):
    if topic:
        content_crew = ContentCrew(topic)
        content_crew.run()