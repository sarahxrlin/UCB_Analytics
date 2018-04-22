# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    hurricane_dictionary = {"ice_cream_1": "Afters",
                            "ice_cream_2": "Ben & Jerry's",
                            "ice_cream_3": "Three Twins"}
    return render_template("index.html", dict=hurricane_dictionary)


if __name__ == "__main__":
    app.run(debug=True)
