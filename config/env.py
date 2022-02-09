import os
if (os.getenv('db_url', None) == None):
	from dotenv import load_dotenv
	load_dotenv()

url = os.getenv('HEROKU_SERVER_URL')
bd_url = os.getenv('DB_URL')
token = os.getenv('TELEGRAM_TOKEN')
port = os.getenv('PORT')
