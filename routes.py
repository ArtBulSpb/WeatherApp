"""
Routes and views for the bottle application.
"""

import json
import os
from bottle import route, view, request, post, redirect
from datetime import date, datetime, timedelta
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

WRITEPATH = 'articles.json'

def parse_date(datestr: str) -> date | str:
    """
    Функция, проверяющая что дата соответствует формату iso и
    находится между нижней границей и текущей датой
    """
    bottom_bound = date(2000, 1, 1)
    try:
        date_val = date.fromisoformat(datestr)
        if date_val < bottom_bound:
            return "Дата не может быть нижней границы: %s" % bottom_bound
        if date.today() < date_val:
            return "Дата не может быть больше текущей"
        return date_val
    except:
        return "Дата не соотвествует формату iso"

class Article:
  def __init__(self, title, author, date):
    self.title = title
    self.author = author
    self.date = date
  
  def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "date": self.date.isoformat()  # Convert date to ISO format string
        }

  @staticmethod
  def from_dict(data):
        return Article(
            title=data["title"],
            author=data["author"],
            date=date.fromisoformat(data["date"])  # Convert ISO format string to date
        )


articles = [] # [Article("Статья1", "Автор1", date.today()), Article("Статья2", "Автор2", date.today())]

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, "reprJson"):
            return o.reprJson()
        else:
            return super().default(o)

@route('/view_articles')
@view('view_articles')
def view_articles(err=""):
    global articles
    if not os.path.exists(WRITEPATH):
        with open(WRITEPATH, 'a+') as json_file:
            json.dump([], json_file, cls=MyEncoder)
    with open(WRITEPATH, 'r+') as json_file:
        articles_dict = json.load(json_file)
        articles = [Article.from_dict(article) for article in articles_dict]
    return dict(
        error=err,
        articles=articles,
        date_today=date.today()
    )

@post('/view_articles', method='post')
def add_article():
    author = request.forms.get('AUTHOR')
    title = request.forms.get('TITLE')
    release_date = request.forms.get('DATE')

    if len(author) < 2 or any(ch.isdigit() for ch in author):
        # Возращаемся на страницу и показываем пользователю ошибку
        return view_articles("Имя автора не должно содеражть цифр и быть меньше двух символов")
    if title == "":
        return view_articles("Название не может быть пустым")
    
    release_date_or_err = parse_date(release_date)
    if isinstance(release_date_or_err, str):
        # Если функция вернула строку, значит это сообщение об ошибке
        return view_articles(release_date_or_err)
    
    
    global articles
    # создаем файл если его нет
    if not os.path.exists(WRITEPATH):
        with open(WRITEPATH, 'a+') as json_file:
            json.dump([], json_file) 
    with open(WRITEPATH, 'r+') as json_file:
        articles_dict = json.load(json_file)
        articles = [Article.from_dict(article) for article in articles_dict]
        articles.append(Article(title, author, release_date_or_err))
        # перезаписываем файл с новыми файлами
        json_file.seek(0)
        json.dump([article.to_dict() for article in articles], json_file)

    print(articles)
    redirect('/view_articles')
