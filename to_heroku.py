import requests
from random import choice
import os
from datetime import date as dt
from bottle import route, run, static_file, view

capitals = ['Tokyo','London','Moscow','Berlin','Paris','Sydney','Oslo', 'Verkhoyansk']
random_cap=choice(capitals)

url = 'https://api.openweathermap.org/data/2.5/weather'
headers = {'Content-Type': 'application/json; charset=utf-8'}


params  = {'q': random_cap,
           'APPID': '*',
           'units':'metric'}

response = requests.post(url, params=params, headers=headers)
result = response.json()

weather =  result['weather'][0]['main']
temp = result['main']['temp']
vis=result['visibility']
wind=result['wind']['speed']



@route("/")
@view("home")
def index():
    return {'random_cap': random_cap, 'dt': dt.today(), 'weather': weather, 'temp': temp, 'vis':vis,'wind': wind}


@route('/static/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root='static/css/')



if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
