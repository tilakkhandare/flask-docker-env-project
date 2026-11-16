import os
from flask import Flask, jsonify

app = Flask(__name__)

# Load secrets safely from environment variables
app.config['JWT_SECRET'] = os.getenv('JWT_SECRET')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

@app.route('/')
def home():
    jwt_loaded = bool(app.config['JWT_SECRET'])
    db_loaded = bool(app.config['DATABASE_URL'])
    return jsonify({
        "status": "running",
        "JWT_SECRET_loaded": jwt_loaded,
        "DATABASE_URL_loaded": db_loaded
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
