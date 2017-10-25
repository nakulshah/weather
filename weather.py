from flask import Flask

app = Flask(__name__)


@app.route('/weather')
def hello_weather():
    return 'Hello This Is Your Weather API!'


if __name__ == '__main__':
    app.run()
