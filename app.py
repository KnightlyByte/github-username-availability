"""
app.py - Simple Flask API to check GitHub username availability.
"""

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# GitHub API URL for user endpoints
GITHUB_API_URL = 'https://api.github.com/users/'


def is_username_available(username):
    """
    Check if a GitHub username is available.

    Parameters:
        username (str): The GitHub username to be checked.

    Returns:
        bool: True if the username is available, False otherwise.
    """
    response = requests.get(GITHUB_API_URL + username)
    return response.status_code == 404


@app.route('/check_username', methods=['GET'])
def check_username():
    """
    API endpoint to check the availability of a GitHub username.

    Query Parameters:
        username (str): The GitHub username to be checked.

    Returns:
        dict: A JSON response containing the availability status.
              {'available': True} if the username is available,
              {'available': False} if the username is already taken,
              {'error': 'Username parameter is missing'} if username is not provided in the query.
    """
    username = request.args.get('username')

    if not username:
        return jsonify({'error': 'Username parameter is missing'}), 400

    if is_username_available(username):
        return jsonify({'available': True})
    else:
        return jsonify({'available': False})


if __name__ == '__main__':
    app.run(debug=True)
