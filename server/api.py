# Import necessary modules and define basic variables
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS, cross_origin
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GAMES_FILE_PATH = os.path.join(BASE, "gateStatus.json")
HISTORY_FILE_PATH = os.path.join(BASE, "history.json")
MAX_HISTORY_LENGTH = 20  # Set the maximum history length as needed
MAX_RETAINED_RECORDS = 5  # Set the maximum number of records to retain

# Create a Flask app and configure settings
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Create the route "/"
@app.route('/')
def main():
    return "Server voor de poort.</a>"

# Create the route "/status"
@app.route('/status', methods=['GET', 'POST'])
@cross_origin()
def games():
    if request.method == 'POST':
        json_data = request.get_json()
        try:
            with open(GAMES_FILE_PATH, 'r') as file:
                file_data = json.load(file)
            file_data.append(json_data)
            with open(GAMES_FILE_PATH, 'w') as file:
                json.dump(file_data, file, indent=4)
            return ""
        except Exception as e:
            print(f"Error writing to the JSON file: {str(e)}")



    if request.method == 'GET':
        return open(GAMES_FILE_PATH).read()


# Create the route "/history"
@app.route('/history', methods=['GET', 'POST'])
@cross_origin()
def history():
    if request.method == 'POST':
        json_data = request.get_json()
        try:
            with open(HISTORY_FILE_PATH, 'r') as file:
                file_data = json.load(file)
            file_data.append(json_data)

            # Check if the history exceeds the maximum length
            if len(file_data) > MAX_HISTORY_LENGTH:
                # Retain the latest MAX_RETAINED_RECORDS records
                file_data = file_data[-MAX_RETAINED_RECORDS:]

            with open(HISTORY_FILE_PATH, 'w') as file:
                json.dump(file_data, file, indent=4)
        except Exception as e:
            return jsonify({"error": str(e)})

    if request.method == 'GET':
        return open(HISTORY_FILE_PATH).read()

# If the file is executed directly, start the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
