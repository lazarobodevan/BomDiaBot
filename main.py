#pip install webdriver-manager
#pip install beautifulsoup4
#pip install selenium
#pip install tweepy

from Controller import Controller

import random
import time
import schedule

def job():
    controller.generateImage(random.choice(urls))

if __name__=="__main__":
    urls =[
        "https://www.youtube.com/watch?v=GAxLcwSQW40",
        "https://www.youtube.com/watch?v=LzFh8b570BU",
        "https://www.youtube.com/watch?v=WAvbHZ-PYM4",
        "https://www.youtube.com/watch?v=nCZNOKD8DCc",
        "https://www.youtube.com/watch?v=JCJzQTCCyBc",
        "https://www.youtube.com/watch?v=evfNT5iRBwo",
        "https://www.youtube.com/watch?v=vXNmWF-hkZk"
    ]


    controller = Controller()
    schedule.every().day.at("07:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
