# Importation des modules nécessaires
from flask import Flask, render_template, request
from urllib.request import urlopen 
import xml.etree.ElementTree as ET
import requests
import xmltodict
import json 

# Clé API pour le service météo
WEATHERAPI_KEY='YOUR_API_KEY'

# Initialisation de l'application Flask
app = Flask(__name__)

# Définition de la route pour la page d'accueil
@app.route("/")
def home():
    # Rendu du template index.html pour la page d'accueil
    return render_template("index.html")

# Définition de la route pour la page météo
@app.route("/weather", methods=["GET", "POST"])
def weather_home():
    # Initialisation de la variable param
    param=None

    # Récupération du nombre de jours de prévision météo à partir des arguments de la requête, par défaut à 3
    number_of_days_forcast=request.args.get("number_of_days_forcast") or 3

    # Récupération de la localisation à partir des arguments de la requête
    location=request.args.get("location")

    # Récupération de la latitude et de la longitude à partir des arguments de la requête
    latitude, longitude = request.args.get("latitude"), request.args.get("longitude")

    # Si une localisation est fournie, elle est utilisée comme paramètre
    if location:
        param=location
    # Si une latitude et une longitude sont fournies, elles sont utilisées comme paramètre
    elif latitude and longitude:
        param=f'{latitude},{longitude}'
    # Si aucune localisation ni latitude/longitude ne sont fournies, la localisation par défaut est 'Burkina'
    else:
        param='Burkina'

    # Construction de l'URL de l'API météo
    api_url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHERAPI_KEY}&q={param}&days={number_of_days_forcast}'

    # Envoi de la requête à l'API météo
    response = urlopen(api_url) 

    # Conversion de la réponse en JSON
    data_json = json.loads(response.read()) 

    # Extraction des informations de localisation, de la météo actuelle et des prévisions météo
    location=data_json['location']
    current_weather = data_json['current']
    forecast_days=data_json['forecast']['forecastday']

    # Rendu du template "weather/index.html" avec les informations de localisation, de la météo actuelle et des prévisions météo
    return render_template("weather/index.html",location=location,current_weather=current_weather,forecast_days=forecast_days)

# Définition de la route pour la page météo avec réponse en XML
@app.route("/weatherXML", methods=["GET", "POST"])
def weather_homeXML():
    # Initialisation de la variable param
    param=None

    # Récupération du nombre de jours de prévision météo à partir des arguments de la requête, par défaut à 3
    number_of_days_forcast=request.args.get("number_of_days_forcast") or 3

    # Récupération de la localisation à partir des arguments de la requête
    location=request.args.get("location")

    # Récupération de la latitude et de la longitude à partir des arguments de la requête
    latitude, longitude = request.args.get("latitude"), request.args.get("longitude")

    # Si une localisation est fournie, elle est utilisée comme paramètre
    if location:
        param=location
    # Si une latitude et une longitude sont fournies, elles sont utilisées comme paramètre
    elif latitude and longitude:
        param=f'{latitude},{longitude}'
    # Si aucune localisation ni latitude/longitude ne sont fournies, la localisation par défaut est 'Burkina'
    else:
        param='Burkina'

    # Construction de l'URL de l'API météo
    api_url = f'http://api.weatherapi.com/v1/forecast.xml?key={WEATHERAPI_KEY}&q={param}&days={number_of_days_forcast}'

    # Envoi de la requête à l'API météo
    response = requests.get(api_url)

    # Conversion de la réponse en dictionnaire
    dict_data = xmltodict.parse(response.content)

    # Conversion du dictionnaire en JSON
    data_json = dict_data['root']

    # Extraction des informations de localisation, de la météo actuelle et des prévisions météo
    location=data_json['location']
    current_weather = data_json['current']
    forecast_days=data_json['forecast']['forecastday']

    # Rendu du template "weather/indexXML.html" avec les informations de localisation, de la météo actuelle et des prévisions météo
    return render_template("weather/indexXML.html",location=location,current_weather=current_weather,forecast_days=forecast_days)