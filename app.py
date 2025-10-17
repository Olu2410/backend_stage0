import os
from flask import Flask, jsonify
import requests
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def get_me():
    cat_fact_api = "https://catfact.ninja/fact"
    fact = None

    try:
        # Fetch cat fact from external API with timeout
        response = requests.get(cat_fact_api, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        fact = data.get("fact", "No cat fact available at the moment.")
    except requests.exceptions.RequestException as e:
        # Handle timeout, connection errors, etc.
        fact = "Unable to fetch a cat fact right now. Please try again later."
        print(f"Error fetching cat fact: {e}")

    # Current UTC timestamp in ISO 8601 format
    timestamp = datetime.now(timezone.utc).isoformat()

    result = {
        "status": "success",
        "user": {
            "email": "olumuyiwa69@yahoo.com", 
            "name": "Olumuyiwa Olu",
            "stack": "Python/Flask"
        },
        "timestamp": timestamp,
        "fact": fact
    }

    return jsonify(result), 200


# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway provides PORT automatically
    app.run(host="0.0.0.0", port=port)