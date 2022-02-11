# Imports
from Bot import bot
from config.Env import URL, PORT, TOKEN
from flask import Flask, render_template, jsonify, Response
from routes.API import api

# SetUp
app = Flask(__name__)

# Routes
app.register_blueprint(api, url_prefix='/api')
@app.route('/')
def hello_world():
	return jsonify({'response': "all good"})
@app.route('/' + TOKEN)
def webhook(update):
	bot.process_update(update)
	return Response(status = 200)

# Start the server
app.run(host=URL, port=PORT)
