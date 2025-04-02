from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import datetime

class CityResearchPoint(BaseModel):
    cities: List[str] = Field(desciption="List of your top 10 cities that best match the user's query")
    match_score: List[float] = Field(description="List of match scores for each city")
    daily_budget: List[int] = Field(description="List of daily budgets for each city")
    forecast_weather: List[str] = Field(description="List of weather forecasts for each city")
    attractions: List[str] = Field(description="List of attractions for each city")
    reason_of_picking: List[str] = Field(description="List of reasons for picking each city")
