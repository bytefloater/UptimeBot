from flask import Flask, render_template
from threading import Thread
import os

appLocation = os.getcwd()

app = Flask('', static_folder=f'{appLocation}/webserver/static', template_folder='webserver')

@app.route('/')
def home():
	return render_template('index.html')

def run():
  app.run(
		host='0.0.0.0',
		port=3000
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()