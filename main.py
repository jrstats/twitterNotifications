# %%
import class_email
import class_twitter
import json

def main():
    with open("./keys.json", "r") as f:
        keys = json.load(f)
    ts = class_twitter.TwitterScraper(keys)
    ts.getTweets()
    html = ts.makeEmailBody()


    host = "mail.privateemail.com"
    port = 465 #TLS: 587; SSL: 465
    email = keys["email_address"]
    password = keys["email_password"]
    emailer = class_email.Emailer(host, port, email, password)

    try:
        msg = emailer.constructEmail("james@robinson.fyi", "Brentford Tweets", ts.makeEmailBody(), True)
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