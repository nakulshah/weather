from flask import Flask, jsonify
from interface.WeatherInfo import WeatherInfo
import json

app = Flask(__name__)


@app.route('/weather')
def hello_weather():
    output = WeatherInfo()
    result = json.dumps(output.__dict__)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
