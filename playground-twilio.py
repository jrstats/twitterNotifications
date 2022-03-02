# %%
import json
from twilio.rest import Client

# %%
with open("./keys.json", "r") as f:
    keys = json.load(f)


twilio_sid = keys["twilio_sid"]
twilio_key = keys["twilio_key"]
client = Client(twilio_sid, twilio_key)

# %%
message = client.messages.create(
    body =  "Testing 1, 2, 3", #Message you send
    from_ = "+14155238886", #Provided phone number
    to =    "+447554131500" #Your phone number
)
message.sid
# %%
