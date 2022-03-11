# %%
import json
import twitter as tw
import pandas as pd
import urllib.parse as p
from io import StringIO


class TwitterScraper:
    def __init__(self, access_token_key, access_token_secret, consumer_key, consumer_secret, id_csv_location="./id.csv"):
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.id_csv_location = id_csv_location
        self.getApi()
        self.getOldTweetIds()

    @classmethod
    def fromDict(cls, keys, id_csv_location="TimerTrigger1/id.csv"):
        access_token_key = keys["access_token_key"]
        access_token_secret = keys["access_token_secret"]
        consumer_key = keys["consumer_key"]
        consumer_secret = keys["consumer_secret"]

        return cls(access_token_key, access_token_secret, consumer_key, consumer_secret, id_csv_location)

    def getApi(self):
        self.api = tw.Api(
            access_token_key=self.access_token_key,
            access_token_secret=self.access_token_secret,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret
        )

    def getTweets(self, oldTweets, filter_terms=["🎟", "ticket", "tickets", "all my bees members"], screen_name="BrentfordFC", count=100):
        self.setOldTweets(oldTweets)
        allTweets = self.api.GetUserTimeline(
            screen_name=screen_name, 
            exclude_replies=True,
            include_rts=False,
            count=count
        )

        filterTweets = [t for t in allTweets if any([x.lower() in t.text.lower() for x in filter_terms])]
        self.newTweets = [t for t in filterTweets if not t.id in self.oldTweetIds]

    def makeEmailBody(self):
        htmlList = []
        for nt in self.newTweets:
            url = nt.urls[0].expanded_url
            htmlList.append(f"<li><a href={url}>{nt.text}</a></li>")
        html = "\n".join(htmlList)
        return f"""<p><ul>{html}</ul></p>"""


    # def writeNewTweets(self):
    #     with open(self.id_csv_location, 'a', newline="") as f:
    #         writer_object = DictWriter(f, fieldnames=["id"])
    #         for t in self.newTweets:
    #             writer_object.writerow({"id": t.id})

    def makeAllTweetIds(self):
        allTweetIds = [[t.id] for t in self.newTweets] + [[x] for x in self.oldTweetIds]
        return pd.DataFrame(allTweetIds, columns=["id"]).to_csv()

    def setOldTweets(self, oldTweets):
        oldTweetsStr = StringIO(oldTweets)
        try:
            self.oldTweetIds = pd.read_csv(oldTweetsStr)["id"].values
        except:
            self.oldTweetIds = []

    def getOldTweetIds(self):
        try:
            self.oldTweetIds = pd.read_csv(self.id_csv_location)["id"].values
        except FileNotFoundError:
            self.oldTweetIds = []

        






# %%
if __name__ == "__main__":
    with open("./keys.json", "r") as f:
        keys = json.load(f)
    ts = TwitterScraper(keys)
    ts.getTweets()
    html = ts.makeEmailBody()

# %%
