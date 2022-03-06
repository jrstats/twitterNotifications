# %%
from . import class_email, class_twitter
import json

def main():
    with open("TimerTrigger1/keys.json", "r") as f:
        keys = json.load(f)
    ts = class_twitter.TwitterScraper.fromDict(keys)
    emailer = class_email.Emailer.fromDict(keys, tls=False)

    ts.getTweets()
    html = ts.makeEmailBody()

    try:
        msg = emailer.constructEmail("james@robinson.fyi", "Brentford Tweets", html, htmlContent=True)
        emailer.sendEmail(msg)
        
    except:
        pass
    else:
        print("email sent")
        ts.writeNewTweets()
        print("tweets written")

# %%
if __name__ == "__main__":
    main()
# %%
