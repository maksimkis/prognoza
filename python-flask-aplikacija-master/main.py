import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/zagreb", methods=["GET"])
def zagreb():
    grad = "Zagreb"

    unit = "metric"

    apikey = "61896784c61a8f3e01d7b087738b95e3"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("zagreb.html", data=data.json())


@app.route("/beli_manastir", methods=["GET"])
def beli_manastir():
    grad = "Beli manastir"

    unit = "metric"

    apikey = "61896784c61a8f3e01d7b087738b95e3"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("beli_manastir.html", data=data.json())


@app.route("/barka", methods=["GET"])
def barka():
    grad = "Barka"

    unit = "metric"

    apikey = "61896784c61a8f3e01d7b087738b95e3"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("barka.html", data=data.json())



if __name__ == '__main__':
    app.run()
