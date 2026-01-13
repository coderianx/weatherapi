from fastapi import FastAPI, Query
from services.weather_services import get_weather
from models.weather import WeatherResponse

app = FastAPI(
    title="Free Weather API",
    description="wttr.in kullanarak ücretsiz hava durumu API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "API is running.",
        "usage": "http://127.0.0.1:8000/weather?city=istanbul",
    }

@app.get("/weather", response_model=WeatherResponse)
def weather(city: str = Query(..., min_length=2)):
    return get_weather(city)
