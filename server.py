from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return f'''<img src="{url_for('static', filename='img/img.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)