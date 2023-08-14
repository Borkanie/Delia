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
import time


app = Flask(__name__)

# Get the path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(script_dir, 'chromedriver.exe')

options = webdriver.ChromeOptions()
#options.add_argument('--headless')

# Set ChromeDriver capabilities
caps = DesiredCapabilities.CHROME.copy()
caps['pageLoadStrategy'] = 'normal'
caps['unhandledPromptBehavior'] = 'accept'
caps['timeout'] = 30  # Set the timeout here (in seconds)

driver = webdriver.Chrome(executable_path=chromedriver_path, options=options,desired_capabilities=caps)
accepted = True

def searchQuery(query,first = True):
    #query = request.args.get('query')

    if not query:
        return jsonify({'error': 'Query parameter "query" is required'}), 400    

    driver.get(f'https://www.google.com/search?q={query}')
    
    
    if first:
        time.sleep(2)
        button_xpath = '/html/body/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]'
        button_element = driver.find_element_by_xpath(button_xpath)

        # Click on the button
        button_element.click()

    html_content = driver.page_source    

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Replace 'your-class-name' with the actual class name you want to target
    carousel = soup.find('g-scrolling-carousel')

    elements = carousel.find_all('a') 

    result = []
    
    for elem in elements:
        children = elem.find_all()
        date = children[7].string
        location = children[5].string
        name = children[3].string
        result.append(Element(name,date,location))
        json = Element(name,date,location)
        json = json.JSON()
        result.append(json)
    return result

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    if not query:
        return jsonify({'error': 'Query parameter "query" is required'}), 400    

    driver.get(f'https://www.google.com/search?q={query}')
    html_content = driver.page_source    

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Replace 'your-class-name' with the actual class name you want to target
    carousel = soup.find('g-scrolling-carousel')

    elements = carousel.find_all('a') 

    result = []
    
    for elem in elements:
        children = elem.find_all()
        date = children[7].string
        location = children[5].string
        name = children[3].string
        result.append(Element(name,date,location))
        json = Element(name,date,location)
        result.append(json)
        
    # Convert the list of custom elements to dictionaries
    elements_json = [element.__dict__ for element in result]

    return jsonify({'elements':elements_json})

if __name__ == '__main__':
    searchQuery("events+in+cluj")
    app.run(debug=True)
    