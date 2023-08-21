from asyncio import wait
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from bs4 import BeautifulSoup
from Element import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebScrapper import WebScrapper
import time
from flask_cors import CORS

app = Flask(__name__)

scrapper = WebScrapper()
# Allow CORS for all domains (*), you can adjust this based on your needs

@app.route('/google', methods=['GET'])
def google():
    event = request.args.get('query')

    if not event:
        return jsonify({'error': 'Query parameter "query" is required'}), 400    

    return scrapper.getFromGoogle(event)

@app.route('/facebook', methods=['GET'])
def facebook():
    event = request.args.get('query')
    
    posts = request.args.get('posts')

    if not event:
        return jsonify({'error': 'Query parameter "query" is required'}), 400    
    print(event)
    if not posts:
        return jsonify({'error': 'Query parameter "posts" is required'}), 400    
    print(posts)
    try:
        return scrapper.getFromFacebook(event,posts)
    except Exception as ex:
        return jsonify({'error': 'Internal error'}), 404    

if __name__ == '__main__':
    #searchQuery("events+in+cluj")
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(debug=True)
    #scrapper.getFromGoogle("Events+in+cluj")
    #scrapper.getFromFacebook("Untold")