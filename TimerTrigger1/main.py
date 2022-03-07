# %%
from azure.storage import blob
from . import class_email, class_twitter, class_blob
import json

def main():
    with open("TimerTrigger1/keys.json", "r") as f:
        keys = json.load(f)
    ts = class_twitter.TwitterScraper.fromDict(keys)
    emailer = class_email.Emailer.fromDict(keys, tls=False)
    blob = class_blob.Blob.fromDict(keys)

    oldTweets = blob.download()
    ts.getTweets(oldTweets)
    if len(ts.newTweets) == 0:
        return

    html = ts.makeEmailBody()

    try:
        msg = emailer.constructEmail("james@robinson.fyi", "Brentford Tweets", html, htmlContent=True)
        emailer.sendEmail(msg)
        
    except:
        pass
    else:
        print("email sent")
        blob.upload(ts.makeAllTweetIds())
        print("tweets written")

# %%
if __name__ == "__main__":
    main()
# %%
