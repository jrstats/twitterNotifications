# %%
import json
import twitter as tw
import pandas as pd
from csv import writer

def filterTweets(tweets, terms, lower=True):
    if lower:
        return [t for t in tweets if any([x.lower() in t.text.lower() for x in terms])]
    else:
        return [t for t in tweets if any([x in t.text for x in terms])]

def checkNewTweets(tweets, idCsvLocation="./id.csv"):
    try:
        oldTweets = pd.read_csv(idCsvLocation)
    except FileNotFoundError:
        print("idCsv not found - all tweets new.")
        return tweets

    return [t for t in tweets if t.id not in oldTweets["id"]]

def writeNewTweets(tweets, idCsvLocation="./id.csv"):
    with open(idCsvLocation, 'a', newline="") as f:
        writer_object = writer(f)
        for t in tweets:
            writer_object.writerow([t.id])

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
# %%
for t in ticketTweets:
    print("----------")
    print(t.text)
    print(t.user.name)
    print(t.created_at)
    print(t.id)
    print([x.text for x in t.hashtags])
# %%

ticketTweetsNew = checkNewTweets(ticketTweets)
writeNewTweets(ticketTweetsNew)
# %%
