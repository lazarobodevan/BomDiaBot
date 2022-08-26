from ImageHandling import ImageHandling
from Scrapping import Scrapping
from Tweeter import Tweeter
class Controller:

    def __init__(self):
        pass

    def generateImage(self, url):
        
        scrap = Scrapping()
        image = ImageHandling()
        tweet = Tweeter()

        comments = scrap.ScrapComment(url)
        random_comment = scrap.getRandomComment(comments)

        generated_image = image.writeImage(random_comment)
        tweet.post_tweet(generated_image)
