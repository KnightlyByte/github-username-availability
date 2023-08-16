# GitHub Username Availability Checker

A simple Flask API to check the availability of a GitHub username using the GitHub API.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)

# Overview

This project provides a minimalistic Flask API that interacts with the GitHub API to determine whether a given GitHub username is available or already taken. It exposes a single API endpoint to perform this check.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KnightlyByte/github-username-availability.git

2. Navigate to the project directory:
    
    ```bash
   cd github-username-availability

3. Install the required dependencies using `pip`:

    ```bash
   pip install -r requirements.txt

## Usage


1. Start the Flask development server:

   ```bash
   python app.py

2. The API server will start, and you can access it at http://localhost:5000/check_username?username=desired_username.

Replace <i>desired_username</i> with the GitHub username you want to check. The script will respond with a JSON object indicating whether the username is available on GitHub or not.

## API Endpoint

#### GET /check_username

Check the availability of a GitHub username.

#### Query Parameters

    username (string, required): The GitHub username to be checked.

#### Response

If the username is available:

```json
{
  "available": true
}
```

If the username is not available (already taken):

```json
{
  "available": false
}
```

If the username query parameter is missing:

```json
{
  "error": "Username parameter is missing"
}
```
