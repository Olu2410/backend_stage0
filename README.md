A simple RESTful API built with Flask that returns my personal profile information and a dynamic cat fact fetched from the Cat Facts API

This project demonstrates how to:

Consume third-party APIs — fetches random cat facts from https://catfact.ninja/fact

Handle errors gracefully — returns fallback messages when the external API is unavailable

Return dynamic data with timestamps  — always returns the current UTC time in ISO 8601 format

Format JSON responses


Create and activate virtual environment:
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

Install dependencies:
pip install -r requirements.txt

Run the app:
python app.py
