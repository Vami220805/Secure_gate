"""
Dit is de flask server die ervoor zorgt dat het dambord, de webInterface en de website met elkaar kunnen comuniceren.
"""

# importeer nodioge modules en defineer alle basis variabelen
from flask import Flask, request, redirect
from flask_cors import CORS, cross_origin
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GAMES_FILE_PATH = os.path.join(BASE, "gateStatus.json")
HISTORY_FILE_PATH = os.path.join(BASE, "history.json")
MAX_HISTORY_LENGTH = 100  # Set the maximum history length as needed


# maak een flas app aan, en verander de instellingen
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# maak de route "/" aan
# als mensen deze route bezoeken krijgen ze een korte tekst te zien
@app.route('/')
def main():
    return "Server voor de poort.</a>"

# maak de route "/games" aan
# als hiernaar gepost wordt dan wordt de json data append naar de games.json file
# als deze route bezoek wordt dan geeft hij de inhoud van games.json terug
@app.route('/status', methods=['GET','POST'])
@cross_origin()
def games():
    if request.method == 'POST':
        json_data = request.get_json()
        with open(GAMES_FILE_PATH,'r') as file:
            file_data = json.load(file)
            file_data.append(json_data)
        with open(GAMES_FILE_PATH,'w') as file:
            json.dump(file_data, file, indent = 4)
        return ""

    if request.method == 'GET':
        return open(GAMES_FILE_PATH).read()
    

@app.route('/history', methods=['GET','POST'])
@cross_origin()
def history():
    if request.method == 'POST':
        json_data = request.get_json()
        # Append the new data to the existing data
        with open(HISTORY_FILE_PATH, 'r') as file:
            file_data = json.load(file)
            file_data.append(json_data)

        if len(file_data) > MAX_HISTORY_LENGTH:
            # If history exceeds the maximum length, overwrite the file
            with open(HISTORY_FILE_PATH, 'w') as file:
                json.dump(file_data, file, indent=4)
        return ""


    if request.method == 'GET':
        return open(HISTORY_FILE_PATH).read()

# als de file direct wordt uitgevoerd dan start de flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)