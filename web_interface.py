from flask import Flask, render_template, request
from threading import Thread
import os
import datetime
import requests


appLocation = os.getcwd()

app = Flask('UptimeBot Web Interface',
            static_folder=f'{appLocation}/webserver/static',
            template_folder='webserver'
            )

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/api/send', methods=['POST'])
def send():
    inputData = request.json
    print(request.json)


    # For all parameters, see README.md
    data = {}
    data["embeds"] = []

    embed = {
        "title": inputData['alertDetails'],
        "color": color(inputData['alertType']),
        "timestamp": formatTime(inputData['alertDateTime']),
        "fields": [
            {
                "name": "**Name**",
                "value": inputData['monitorFriendlyName'],
            },
            {
                "name": "**Destination**",
                "value": inputData['monitorURL'],
            },
            {
                "name": "**Type**",
                "value": inputData['alertTypeFriendlyName'],
            }
        ]
    }
    data["embeds"].append(embed)

    if inputData['requestSecret'] == os.environ.get('requestSecret'):
        url = os.environ.get('discordWebHookURL')
        result = requests.post(url, json=data, headers={"Content-Type": "application/json"})
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

    return 'OK'


def run():
    app.run(
        host='0.0.0.0',
        port=3000
    )


def startServer():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()


def formatTime(unixTimestamp):
    '''
    Converts Unix Timestamp to: YYYY:MM:DDTHH:MM:ss.SSSZ
    '''
    try:
        time = datetime.datetime.fromtimestamp(int(unixTimestamp))
        time = time.strftime("%Y-%m-%dT%H:%M:%SZ")
        return time
    except ValueError:
        print('Unable to parse timestamp:', unixTimestamp)
        return 0


def color(alertType):
    '''
    alertType Values: 1 - Down
                      2 - Up
                      3 - SSL Expiration (not used elsewhere in code)
    '''
    if alertType == '1':
        color = int('0xE00000', 16)
    elif alertType == '2':
        color = int('0x36ab42', 16)
    elif alertType == '3':
        color = int('0x333fc1', 16)
    else:
        color = int('0x000000', 16)

    return color
