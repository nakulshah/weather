from flask import Flask, jsonify
from interface.WeatherInfo import WeatherInfo

app = Flask(__name__)


@app.route('/weather')
def hello_weather():
    output = WeatherInfo()
    return jsonify(output.__dict__)


if __name__ == '__main__':
    app.run()
