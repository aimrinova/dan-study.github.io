# filename: weather_data.py
# -*- coding: utf-8 -*-
# Author:  Daniel Schubert using Visual Studio Code and .venv with Python 3.13.1
# Created on: 2025-04-13
# I looked up the source code of the library to understand how it works, and it works with nearest
# and last observation data
# It is not in realtime, but a good alternative to the OpenWeatherMap API

import asyncio
import python_weather
from typing import Tuple
from datetime import datetime

async def get_temperature(location) -> Tuple[int, datetime]:
    """Fetch the current temperature for a given location.
    @class Client: creates a session with this @url='https://wttr.in/Berlin?format=j1'
    additionally client.py imports the library's class Forecast to get the weather data
    """
    try:
        async with python_weather.Client() as client: # makes sure to close the session after use
            # Fetch the weather data for the specified location
            # The location can be a city name, coordinates, or a postal code
            weather = await client.get(location)
            # Extract the temperature and datetime from the weather data
            return weather.temperature, weather.datetime
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your internet connection or the location name.")
        raise

if __name__ == "__main__":
    # Get the temperature for Berlin
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    temperature, local_time = asyncio.run(get_temperature("Berlin"))
    print(f"The temperature in Berlin is {temperature}°C")
    print(f"Latest Local time: {local_time}")
