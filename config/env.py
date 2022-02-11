import os
if (os.getenv('db_url', None) == None):
	from dotenv import load_dotenv
	load_dotenv()

url = os.getenv('HEROKU_SERVER_URL', 'localhost')
db_url = os.getenv('DB_URL')
db_name = os.getenv('DB_NAME')
token = os.getenv('TELEGRAM_TOKEN')
port = os.getenv('PORT', 3000)
