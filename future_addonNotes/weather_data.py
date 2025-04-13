# filename: weather_data.py
# -*- coding: utf-8 -*-
# Author:  Daniel Schubert using Visual Studio Code and .venv with Python 3.13.1
# Created on: 2025-04-12
# I looked up the source code of the library to understand how it works, and it works with nearest and last observation data
# It is not in realtime, but a good alternative to the OpenWeatherMap API

import asyncio
import python_weather
from typing import Tuple, Optional
from datetime import datetime

async def get_temperature(location) -> Tuple[int, datetime, Optional[int]]:
    """Fetch the current temperature for a given location.
    @class Client: creates a session with this @url='https://wttr.in/Berlin?format=j1'
    additionally client.py imports the library's class Forecast to get the weather data
    """
    try:
        async with python_weather.Client() as client: # makes sure to close the session after use
            # Fetch the weather data for the specified location
            # The location can be a city name, coordinates, or a postal code
            weather = await client.get(location)
            # Initialize default values for hourly_temperature and hourly_time
            hourly_temperature = None
            # Assuming you want to access the first daily forecast's temperature
            if weather.daily_forecasts[0].hourly_forecasts:
                hourly_forecasts = weather.daily_forecasts[0].hourly_forecasts[0]
                hourly_temperature = hourly_forecasts.temperature
            return weather.temperature, weather.datetime, hourly_temperature
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your internet connection or the location name.")
        raise

if __name__ == "__main__":
    # Get the temperature for Berlin-Bezirk Neukölln
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    temperature, local_time, hourly_temp= asyncio.run(get_temperature("Berlin-Bezirk Neukölln"))
    print(f"The temperature in Berlin-Bezirk Neukölln is {temperature}°C")
    print(f"Latest Local time: {local_time}")
    print(f"Last Hourly temperature: {hourly_temp}°C")
