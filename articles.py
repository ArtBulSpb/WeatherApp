import json
import os
from bottle import route, view, request, post, redirect
from typing import Union
from datetime import date

WRITEPATH = 'articles.json'

def parse_date(datestr: str) -> Union[date, str]:
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
  def __init__(self, title, author, description, date):
    self.title = title
    self.author = author
    self.description = description
    self.date = date

  # метод для серилизации в json
  def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "date": self.date.isoformat()  # Convert date to ISO format string
        }

  # метод для десериализации
  @staticmethod
  def from_dict(data):
        return Article(
            title=data["title"],
            author=data["author"],
            description=data["description"],
            date=date.fromisoformat(data["date"])  # Convert ISO format string to date
        )

def get_articles():
    # если файл не существует, создаем, записываем пустой список и возвращаем его
    if not os.path.exists(WRITEPATH):
        with open(WRITEPATH, 'a+') as json_file:
            json.dump([], json_file)
            return []
    with open(WRITEPATH, 'r+') as json_file:
        articles_dict = json.load(json_file)
        return [Article.from_dict(article) for article in articles_dict]

def set_articles(articles):
    with open(WRITEPATH, 'r+') as json_file:
        json_file.seek(0)
        json.dump([article.to_dict() for article in articles], json_file)

@route('/view_articles')
@view('view_articles')
def view_articles(err=""):
    articles = get_articles()
    return dict(
        error=err,
        articles=articles,
        date_today=date.today()
    )

@post('/view_articles', method='post')
def add_article():
    author = request.forms.get('AUTHOR')
    title = request.forms.get('TITLE')
    descrtipion = request.forms.get('DESCRIPTION')
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
    
    articles = get_articles()
    articles.insert(0, Article(title, author, descrtipion, release_date_or_err))
    set_articles(articles)

    redirect('/view_articles')