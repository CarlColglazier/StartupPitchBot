import random
import inflect
import tweepy
import pandas as pd

p = inflect.engine()

with open("secret.txt") as n:
    secret = n.read().splitlines()

auth = tweepy.OAuthHandler(secret[0], secret[1])
auth.set_access_token(secret[2], secret[3])

api = tweepy.API(auth)

unicorns = pd.read_csv("unicorns2.txt", names=["company", "views"])

with open("nouns.txt") as n:
    nouns = n.read().splitlines()

message = "{} for {}.".format(
    unicorns.sample(weights="views").iloc[0]["company"],
    p.plural(random.choice(nouns))
)

print(message)
api.update_status(message)
