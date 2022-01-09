# %%
import json
import twitter as tw


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
    screen_name="richardosman", 
    exclude_replies=True, 
    include_rts=False,
    count=100
)
# %%
t = tweets[0]
print(t.text)
print(t.user.name)
print(t.created_at)
print([x.text for x in t.hashtags])
# %%

# from trafilatura import feeds
# mylist = feeds.find_feed_urls('https://www.theguardian.com/')