
import os
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:5001"
)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Kubernetes Full Stack App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            text-align: center;
            padding: 60px 20px;
        }
        .container {
            background: white;
            padding: 35px;
            max-width: 650px;
            margin: auto;
            border-radius: 12px;
            box-shadow: 0 4px 15px #0002;
        }
        h1 { color: #2563eb; }
        .result {
            background: #dcfce7;
            padding: 20px;
            border-radius: 8px;
            margin-top: 25px;
        }
        .error {
            background: #fee2e2;
            padding: 20px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Kubernetes Full Stack Application</h1>
        <h2>Flask Frontend</h2>
        <p>Welcome! Your Flask frontend is running.</p>
        <div class="{{ status }}">
            <h3>Express Backend Response</h3>
            <p>{{ message }}</p>
        </div>
        <p>Deployment: Minikube Kubernetes</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    try:
        response = requests.get(
            f"{BACKEND_URL}/api/message",
            timeout=5
        )
        response.raise_for_status()

        data = response.json()
        message = data.get("message", "No message received")

        return render_template_string(
            HTML,
            message=message,
            status="result"
        )

    except requests.RequestException as error:
        return render_template_string(
            HTML,
            message=f"Backend connection failed: {error}",
            status="error"
        ), 503


@app.route("/health")
def health():
    return {"status": "healthy", "service": "flask-frontend"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
