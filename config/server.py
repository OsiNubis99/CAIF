from bot import bot, updater
from env import url, port
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
#    return render_template('index.html')
	return jsonify({'response': "all good"})

if __name__ == '__main__':
    app.run(host=url, port=port)
