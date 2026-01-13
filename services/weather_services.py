import requests
from fastapi import HTTPException
from models.weather import WeatherResponse

BASE_URL = "https://wttr.in"

def get_weather(city: str) -> WeatherResponse:
    url = f"{BASE_URL}/{city}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            params={"format": "j1"},
            headers=headers,
            timeout=10
        )
    except requests.RequestException:
        raise HTTPException(
            status_code=500,
            detail="Hava durumu servisine bağlanılamadı"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Şehir bulunamadı"
        )

    try:
        data = response.json()
        current = data["current_condition"][0]
    except (KeyError, IndexError, ValueError):
        raise HTTPException(
            status_code=500,
            detail="Hava durumu verisi okunamadı"
        )

    return WeatherResponse(
        city=city.title(),
        temperature=float(current["temp_C"]),
        description=current["weatherDesc"][0]["value"]
    )
