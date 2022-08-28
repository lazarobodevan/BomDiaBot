from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

import time
import random
import os

class Scrapping:

    def __init__(self):
        pass

    def ScrapComment(self, url):
        while True:
            option = webdriver.FirefoxOptions()
            #option.add_argument("-remote-debugging-port=9224")
            option.add_argument("-headless")
            option.add_argument("-disable-gpu")
            option.add_argument("-no-sandbox")
            binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

            driver = webdriver.Firefox(
                firefox_binary=binary,
                executable_path= GeckoDriverManager().install(),
                options=option)

            driver.get(url)
            prev_h = 0
            
            height = driver.execute_script("""
                    function getActualHeight() {
                        return Math.max(
                            Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                            Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                            Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );
                    }
                    return getActualHeight();
                """)
            driver.execute_script(f"window.scrollTo({prev_h},{prev_h + 200})")
            time.sleep(15)
            prev_h +=600  
                
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.close()
            comment_div = soup.select("#content #content-text")
            comment_list = [x.text for x in comment_div]
            print(comment_list)
            if comment_list:
                return comment_list
            print("Erro")

    def getRandomComment(self, comment_list):
        random_comment = comment_list[random.randint(0,len(comment_list)-1)]
        while len(random_comment) > 200:
            random_comment = comment_list[random.randint(0,len(comment_list)-1)]
        return random_comment