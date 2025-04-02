from crewai import Task
from textwrap import dedent
from datetime import date
from typing import List
from crew import CityResearchPoint
#from crewai.project import task
class TripTasks:

    #@task
    def identify_task(
        self,
        agent: str,
        origin: str,
        travel_type: str,
        budget: str,
        month: str,
        region: str,
        activities: List,
    ):

        return Task(
            description=dedent(
                f"""
                Analyze and select the 10 best city for the trip based 
                on specific criteria such as weather patterns, seasonal
                events, and travel costs. This task involves comparing
                multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and
                overall travel expenses. 
                
                Your final answer must be a detailed
                report on the chosen city, and everything you found out
                about it, including the actual flight costs, weather 
                forecast and attractions.
                {self.__tip_section()}

                Traveler type: {travel_type}
                Trip budget {budget}
                Trip Date:: {month}
                Trip region: {region}
                Traveling from: {origin}
                Traveler Interests: {activities}
            """
            ),
            agent=agent,
            #expected_output="A list with bullet points of the 10 best cities to visit",
            output_json=CityResearchPoint,
        )
    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"
