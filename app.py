# app.py

from flask import Flask, request, jsonify, render_template
from URL_shortener import URLShortener

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    url = data.get('url')
    
    url_shortener = URLShortener()
    result = url_shortener.shorten_url(url)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False)
