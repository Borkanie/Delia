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
from selenium.webdriver.common.keys import Keys
import numpy as np
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



class WebScrapper:
    def __init__(self) -> None:
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

        self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=options,desired_capabilities=caps)
        # Open a new tab
        self.driver.execute_script("window.open('', '_blank');")

        self.logInOnFacebook()
        time.sleep(1)

    def getFromGoogle(self,query:str) -> str:

        # Switch to the second tab
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.driver.get(f'https://www.google.com/search?q={query}')
        html_content = self.driver.page_source    

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
        return ""
        #return jsonify({'elements':elements_json})

    def logInOnFacebook(self) -> None:
        
        # Switch to the second tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        # Navigate to the Facebook login page in the second tab
        self.driver.get('https://www.facebook.com')

        time.sleep(3)
        button_xpath = '/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[1]'

        wait = WebDriverWait(self.driver, 10)
        button_element = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        # Click on the button
        button_element.click()
        
        # Perform the login on the second tab
        email_input = self.driver.find_element_by_id('email')
        password_input = self.driver.find_element_by_id('pass')

        email_input.send_keys('dnd_ma_joc_cs@yahoo.com')  # Replace with your email
        password_input.send_keys('Qweasdzxc123halo02*')        # Replace with your password
        password_input.send_keys(Keys.ENTER)

        # Do other actions on the second tab if needed

    def getFromFacebook(self,query:str,posts=5) -> str:

        # Switch to the second tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.get(f"https://www.facebook.com/search/posts/?q={query}")

        
        postlist_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div'

        wait = WebDriverWait(self.driver, 10)
        postlist_element = wait.until(EC.presence_of_element_located((By.XPATH, postlist_xpath)))
        time.sleep(2)
        result = []

        # Find all direct descendant elements of the parent element
        descendant_elements = postlist_element.find_elements(By.XPATH, '*')

        # Process each descendant element
        index = 0
        while(len(result)<int(posts)):
            oldIndex = len(descendant_elements)
            descendant_elements = postlist_element.find_elements(By.XPATH, '*')
            for i in range(index,len(descendant_elements)):
                elem = self.getPost(descendant_elements[i])
                if elem is not None:
                    result.append(elem)
                    if len(result)==posts:
                        return jsonify({"posts":result})
            index = oldIndex

        return jsonify({"posts":result})

    def getPost(self,httpElement) -> str:
        try:
            # Scroll to the element using an actions chain
            actions = ActionChains(self.driver)
            actions.move_to_element(httpElement)
            actions.perform()
            result = ""
            title_xpath="div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[2]/div/div[2]/div/div[1]/span/h3/div/span/a/span"
        
            title = httpElement.find_element(By.XPATH,title_xpath)
            text_xpath = "div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[3]/div[1]/div/div/div/span"

            text = httpElement.find_element(By.XPATH,text_xpath)

            image_xpath = "div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[3]/div[2]/div[1]/a/div[1]/div/div/div/img"
            image_source = None
        
            # Define a timeout for waiting
            timeout = 1  # in seconds

            # Wait up to the defined timeout for the element to exist
            element = WebDriverWait(httpElement, timeout).until(
                EC.presence_of_element_located((By.XPATH, image_xpath))
            )

            # Element exists, do something with it
            image_source = element.get_attribute('src')

        except TimeoutException:

            result = {
            "title" : title.text,
            "text" : text.text,
            "image" : "None",
            }
            return result

        except Exception:

            return None

        result = {
            "title" : title.text,
            "text" : text.text,
            "image" : image_source
        }
        return result