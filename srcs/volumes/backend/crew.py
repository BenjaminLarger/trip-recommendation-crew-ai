from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from typing import List


class CityResearchPoint(BaseModel):
    """
    Structure of the agent output expected
    """

    city: List[str] = Field(description="City name")
    country: List[str] = Field(description="Country name")
    match_score: List[float] = Field(description="Match score for the city")
    weather: List[str] = Field(
        description="Weather forecast in the city at the corresponding month"
    )
    events: List[str] = Field(
        description="Events happening in the city at the corresponding month"
    )
    travel_cost: List[float] = Field(description="Travel cost to the city")
    daily_budget: List[float] = Field(description="Daily budget for the trip")


@CrewBase
class LatestAiDevelopmentCrew:
    @agent
    def city_selector_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["city_selector_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @task
    def city_selector_task(self) -> Task:
        return Task(
            config=self.tasks_config["city_selector_task"],
            output_json=CityResearchPoint,
        )

    @crew
    def crew(self) -> CrewBase:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
