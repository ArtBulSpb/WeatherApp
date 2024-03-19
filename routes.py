"""
Routes and views for the bottle application.
"""

from bottle import route, view, request
from datetime import datetime
from enum import Enum

class Weather(Enum):
    CLOUDY = 'static\images\cloudy.png'
    SUNNY = 'static\images\sunny.png'

class CityWeather:
  def __init__(self, weather, day_temperature, night_temperature):
    self.weather = weather
    self.day_temperature = day_temperature
    self.night_temperature = night_temperature

cities = ["Санкт-Петербург", "Москва"]

city_to_weather = {"Санкт-Петербург" : CityWeather(Weather.CLOUDY, 5, -1),
                   "Москва" : CityWeather(Weather.SUNNY, 10, 2)}

def show_weather(weather: Weather) -> str:
    if weather == Weather.CLOUDY:
        return "Пассмурно"
    else:
        return "Солнечно"

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        cities=cities
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Контакты',
        message='',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='О нас',
        message='',
        year=datetime.now().year
    )

@route('/city_weather')
@view('city_weather')
def city_weather():
    try:
        city_index = int(request.GET.get('city', '').strip())
        city = cities[city_index]
        weather = city_to_weather[city]
        return dict(
            title='Погода в городе: ' + city,
            message='',
            year=datetime.now().year,
            weather=weather,
            weather_show=show_weather(weather.weather)
        )
    except:
        return '<h1>Запрашиваемый город не найден</h1>'
