# Flask Weather Application

This is a simple Flask application that uses the WeatherAPI to fetch and display weather data in both JSON and XML formats.

## Features

- Fetch current weather data
- Fetch weather forecast for the next few days
- Support for different locations
- Support for latitude and longitude input
- Fetch data in JSON format
- Fetch data in XML format and convert it to JSON

## Code Overview

The application is built with Flask and uses the `requests` and `urllib.request` modules to send requests to the WeatherAPI. The `json` and `xmltodict` modules are used to parse the response from the API.

The application defines two routes, `/weather` and `/weatherXML`, which fetch weather data in JSON and XML formats respectively. Both routes accept query parameters for location, latitude, longitude, and the number of forecast days.

## Installation

1. Clone this repository

git clone https://github.com/yourusername/flask-weather-app.git

pip install -r requirements.txt

For Unix/Linux
export FLASK_APP=app.py

For Windows
set FLASK_APP=app.py

4. Run the application

flask run


## Usage

- Visit `http://localhost:5000` to access the application.
- Use the `/weather` endpoint to fetch weather data in JSON format. You can provide location, latitude and longitude as query parameters.
- Use the `/weatherXML` endpoint to fetch weather data in XML format, which is then converted to JSON.

