from temp_api import todayTemp
from movie_api import callMoveApi
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", movies = callMoveApi(), today_temp = todayTemp())

if __name__ == "__main__":
    app.run(debug=True)