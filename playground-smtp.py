# %%
import smtplib
import json
from email.message import EmailMessage

# %%
with open("./keys.json", "r") as f:
    keys = json.load(f)

host = "mail.privateemail.com"
port = 465#TLS: 587; SSL: 465

EMAIL = keys["email_address"]
PASSWORD = keys["email_password"]

msg = EmailMessage()
msg["Subject"] = "TEST EMAIL"
msg["To"] = "james@robinson.fyi"
msg["From"] = EMAIL
msg.set_content("Hello, world!")
# msg.add_alternative("", subtype="html")

# %%
with smtplib.SMTP_SSL(host, port) as smtp:
    # login
    smtp.login(EMAIL, PASSWORD)

    # send email
    smtp.send_message(msg)
# %%
