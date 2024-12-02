# OIM3600-Final-Project
 ## Comp Sci Final Project - Suphadit (Sev) Chansrichawla & Kai Wattanabe

# Project Overview

This project is a web application that allows users to predict the scores of soccer matches and calculates the accuracy of their predictions based on actual match results. The application integrates with the football-data.org API to fetch live match data and provides a user-friendly interface to input predictions. This is meant to be a friendly website that can be used by soccer/footbal fans to have a friendly place to make predictions on upcoming games and be shown an accurate winner between friends.


# Usage Guidelines
	1.	Run app.py program and navigate to http://127.0.0.1:5000 on preffered browser
    2.  Navigate to the homepage to view a list of upcoming soccer matches.
	3.	Click the “Make a Prediction” link to go to the prediction form.
	4.	Enter the home team, away team, and your predicted scores.
    5.  Repeate the step for all players, clicking 'Finish' when all player predictions are inputted
	6.	Submit the form to view the actual scores and your prediction accuracy.
	7.	The app calculates the accuracy of predictions for all participants and determines the winner.


# Dependencies:
    1. Flask: For building the web application.
    2. python-dotenv: To manage sensitive environment variables like the API key.
        - python3 -m pip install flask python-dotenv
    3. urllib.request: To make API requests and fetch match data.


# Project Struture #Created using OpenAI Chat-GPT
project

├── app.py                  # Main Flask application
├── .env                    # Environment variables (excluded from version control)
├── templates/              # HTML templates for the web application
│   ├── index.html          # Displays upcoming matches
│   ├── predict.html        # Form for user predictions
│   ├── results.html        # Displays prediction results
│   ├── final_results.html  # Displays final results, accuracy, and winner
├── static/                 # Static files (CSS, JavaScript)
│   ├── styles.css          # Styling for the web app
├── .gitignore              # Excludes sensitive files from version control
├── README.md               # Project documentation


# Collaboration Information:
    1. Members:
        - Kai Wattanabe
            • Came up with the project idea and helped craft the proposal.
	        •	Added the unique feature to the application by allowing multiple players to make predictions and integrating a system to calculate and display accuracy.
	        •	Assisted in designing the logic for determining the winner based on prediction accuracy.
        - Suphadit (Sev) Chansrichawla
            •	Focused on API integration, sourcing different possible APIs with the help of OpenAI to access live soccer match data.
	        •	Developed the HTML templates to ensure the application’s interface was user-friendly and visually appealing.
	        •	Worked on displaying data dynamically on the website, ensuring the application provided real-time updates.
        


# Acknowledgements: OpenAI/ChatGPT Assistance
    We used OpenAI to help us in working with APIs, building on our previous knowledge on api with the api homework, we utilized Chatgpt to understand how to do with apis that require a key, so for the function def fetch_match_data():, there is usage of AI assistance.

    For some more assistance, ChatGPT helped with input requests from the user; with the @app.route('/') functions and how to incorporate into our project, as well as the usage of POST in order to specify the type of action the client wants to preform

    Lastly we used ChatGpt in its assistance to create the .env file and .gitignore file to hide the API key and still have it function without commiting it

# Reflection:
    This Project has been an extremely fun and enjoyable process being able to design a project that we are both interested in, and something that we can be proud of. It was definitely challenging working with external APIs, not knowing why at times the API would not coorporate or at times when the app.py would not work and go to the results page for example. Overall this whole project has been an amazing learning experience, and while it was definitely excruciating at times when it would not work, it was a fun and enjoyable challenge that put our knowledge of what we learned throughout the class to the test.
