# %%
import json
import twitter as tw
import pandas as pd
from csv import DictWriter



def checkNewTweets(tweets, idCsvLocation="./id.csv"):
    try:
        oldTweets = pd.read_csv(idCsvLocation)
        return [t for t in tweets if not t.id in oldTweets["id"].values]
    except FileNotFoundError:
        print("idCsv not found - all tweets new.")
        return tweets

def writeNewTweets(newTweets, idCsvLocation="./id.csv"):
    with open(idCsvLocation, 'a', newline="") as f:
        writer_object = DictWriter(f, fieldnames=["id"])
        for t in newTweets:
            writer_object.writerow({"id": t.id})

    return None
# %%
with open("./keys.json", "r") as f:
    keys = json.load(f)

# %%
api = tw.Api(
    access_token_key=keys["access_token_key"],
    access_token_secret=keys["access_token_secret"],
    consumer_key=keys["consumer_key"],
    consumer_secret=keys["consumer_secret"]
)
# %%

tweets = api.GetUserTimeline(
    screen_name="BrentfordFC", 
    exclude_replies=True, 
    include_rts=False,
    count=100
)
# %%
ticketTerms = ["🎟", "ticket", "tickets", "all my bees members"]
ticketTweets = filterTweets(tweets, ticketTerms)
ticketTweetsNew = checkNewTweets(ticketTweets)
writeNewTweets(ticketTweetsNew)
# %%
