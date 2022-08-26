import tweepy
import config
class Tweeter:
    def __init__(self):
        pass

    def authenticate(self):
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth)
        
        return api
        
    def post_tweet(self, image):
        try:
            api = self.authenticate()
            api.update_status_with_media("", 'bomdia.jpg', file=image)
        except:
            print("Erro")
