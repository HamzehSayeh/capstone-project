from flask import jsonify
from . import create_app

app = create_app()

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask Docker Demo!")
