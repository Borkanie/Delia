from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

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


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    if not query:
        return jsonify({'error': 'Query parameter "query" is required'}), 400    

    driver.get(f'https://www.google.com/search?q={query}')
    html_content = driver.page_source

    return jsonify({'html': html_content})

if __name__ == '__main__':
    app.run(debug=True)