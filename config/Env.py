# Imports
import os

# SetUp
if (os.getenv('DB_URL', None) == None):
	from dotenv import load_dotenv
	load_dotenv()

# Vars
URL = os.getenv('HEROKU_SERVER_URL',"localhost")
DB_URL = os.getenv('DB_URL')
DB_NAME = os.getenv('DB_NAME')
TOKEN = os.getenv('TELEGRAM_TOKEN')
PORT = os.getenv('PORT', 3000)
