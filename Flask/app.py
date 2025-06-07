from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Hello from Docker!</h1>
    <p>Current time: {current_time}</p>
    <p>This Python app is running inside a Docker container!</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 