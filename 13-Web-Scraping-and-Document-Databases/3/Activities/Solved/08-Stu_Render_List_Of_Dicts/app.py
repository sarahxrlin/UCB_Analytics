# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template


@app.route("/")
def index():
    music_fest_cities = [{"Coachella": "Indio"}, {"Lollapalooza": "Chicago"}, {"Electric Zoo": "New York"}]
    return render_template("index.html", list=music_fest_cities)


if __name__ == "__main__":
    app.run(debug=True)
