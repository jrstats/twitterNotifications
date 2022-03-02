# %%
import json
import twitter as tw
import pandas as pd
import urllib.parse as p
from csv import DictWriter


class TwitterScraper:
    def __init__(self, keys, id_csv_location="./id.csv"):
        self.keys = keys
        self.id_csv_location = id_csv_location
        self.getApi()
        self.getOldTweetIds()

    def getApi(self):
        self.api = tw.Api(
            access_token_key=self.keys["access_token_key"],
            access_token_secret=self.keys["access_token_secret"],
            consumer_key=self.keys["consumer_key"],
            consumer_secret=self.keys["consumer_secret"]
        )

    def getTweets(self, filter_terms=["🎟", "ticket", "tickets", "all my bees members"], screen_name="BrentfordFC", count=100):
        allTweets = self.api.GetUserTimeline(
            screen_name=screen_name, 
            exclude_replies=True,
            include_rts=False,
            count=count
        )

        filterTweets = [t for t in allTweets if any([x.lower() in t.text.lower() for x in filter_terms])]
        self.newTweets = [t for t in filterTweets if not t.id in self.oldTweetIds]

    def makeEmailBody(self):
        urlList = [x.urls[0].expanded_url for x in self.newTweets]
        htmlList = [f"""<iframe border=0 frameborder=0 height=250 width=550 src="https://twitframe.com/show?url={p.quote(x)}"></iframe>""" for x in urlList]
        html = "\n".join(htmlList)
        return f"""<p>{html}</p>"""


    def writeNewTweets(self):
        with open(self.id_csv_location, 'a', newline="") as f:
            writer_object = DictWriter(f, fieldnames=["id"])
            for t in self.newTweets:
                writer_object.writerow({"id": t.id})



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
