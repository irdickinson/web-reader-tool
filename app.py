from flask import Flask, render_template, request, jsonify, session
import json
import os
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)