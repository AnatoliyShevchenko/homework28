from flask import (Flask, render_template)
# import urllib.request
# import json
import requests
from requests.models import Response


app = Flask(__name__)

url = "https://www.freetogame.com/api/games?platform=pc"
r: Response = requests.get(url)
data = r.json()
_list_of_games = []
_posters = []
for element in data:
    _list_of_games.append(element.get("title"))
    _posters.append(element.get("thumbnail"))


@app.route('/')
def index():
    return f'<h3>This is the page about my homework</h3>\
        <a href="http://localhost:8085/about">Ссылка на страницу обо мне</a><br>\
            <a href="http://localhost:8085/games">Ссылка на страницу c моими любимыми видеоиграми</a><br>\
            <a href="http://localhost:8085/films">Ссылка на страницу с моими любимыми фильмами</a><br>\
            <a href="http://localhost:8085/all-games">Ссылка на страницу с играми по JSON</a>'

@app.route('/about')
def about():
    return render_template('/shap/about.html')

@app.route('/games')
def games():
    return render_template('/shap/games.html')

@app.route('/films')
def films():
    return render_template('/shap/films.html')

@app.route('/all-games')
def all_games():
    return render_template(
        '/shap/all-games.html', 
        listgames=_list_of_games,
        posterslist=_posters
        )

if __name__ == "__main__":
    app.run(port=8085, debug=True)