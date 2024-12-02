from flask import Flask, render_template, request, session
import urllib.request
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# API details
API_URL = "https://api.football-data.org/v4/matches"
API_KEY = os.getenv("API_KEY")

# Store predictions
user_predictions = []

def fetch_match_data():
    headers = {"X-Auth-Token": API_KEY}
    req = urllib.request.Request(API_URL, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            matches = json.loads(data)
            return matches
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

@app.route('/')
def index():
    global user_predictions  # Access the global list
    user_predictions = []  # Clear all previous predictions
    matches = fetch_match_data()
    if matches and "matches" in matches:
        return render_template('index.html', matches=matches["matches"])
    else:
        return render_template('index.html', matches=[])

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'finish' in request.form:  # Check if the 'Finish' button was pressed
            return render_template('results.html', predictions=user_predictions)

        # Process player prediction
        team1 = request.form.get('team1')
        team2 = request.form.get('team2')
        predicted_score1 = int(request.form.get('score1', 0))
        predicted_score2 = int(request.form.get('score2', 0))
        username = request.form.get('username', 'Anonymous')

        # Store the prediction
        user_predictions.append({
            'username': username,
            'team1': team1,
            'team2': team2,
            'predicted_score1': predicted_score1,
            'predicted_score2': predicted_score2
        })

        return render_template('predict.html', message="Prediction added! Add another player or finish.")
    
    return render_template('predict.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        # Retrieve actual results from the form
        actual_team1 = request.form.get('team1', 'Team 1')
        actual_team2 = request.form.get('team2', 'Team 2')
        actual_score1 = int(request.form.get('actual_score1', 0))
        actual_score2 = int(request.form.get('actual_score2', 0))

        # Maximum accuracy and possible difference
        max_accuracy = 100
        max_possible_diff = 10  # Adjust this based on scoring range

        # Calculate accuracy for each player
        for prediction in user_predictions:
            predicted_score1 = prediction['predicted_score1']
            predicted_score2 = prediction['predicted_score2']

            # Total difference
            total_diff = abs(predicted_score1 - actual_score1) + abs(predicted_score2 - actual_score2)

            # Accuracy formula
            prediction['accuracy'] = max(max_accuracy - (total_diff / max_possible_diff) * max_accuracy, 0)

        # Redirect to final results page
        return render_template(
            'final_results.html',
            predictions=user_predictions,
            actual_scores={
                'team1': actual_team1,
                'team2': actual_team2,
                'actual_score1': actual_score1,
                'actual_score2': actual_score2,
            }
        )
    return render_template('results.html', predictions=user_predictions)

@app.route('/final_results')
def final_results():
    return render_template('final_results.html', predictions=user_predictions)

if __name__ == '__main__':
    app.run(debug=True)

