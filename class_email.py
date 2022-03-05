# %%
import smtplib
from email.message import EmailMessage

class Emailer:
    def __init__(self, host, port, email, password):
        self.host = host
        self.port = port
        self.email = email
        self.password = password

    @classmethod
    def fromDict(cls, keys, tls=False):
        host = keys["email_host"]
        port = keys["email_port_tls"] if tls else keys["email_port_ssl"]
        email = keys["email_address"]
        password = keys["email_password"]
        return cls(host, port, email, password)

    def constructEmail(self, to, subject, body, htmlContent=False):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["To"] = to
        msg["From"] = self.email

        if htmlContent:
            msg.add_alternative(body, subtype="html")
        else:
            msg.set_content(body)

        return msg

    def sendEmail(self, msg):
        try:
            with smtplib.SMTP_SSL(self.host, self.port) as smtp:
                smtp.login(self.email, self.password)
                smtp.send_message(msg)
        except Exception as e:
            print("Sending email failed with following error")
            print(e)

        
# %%
if __name__ == "__main__":
    import json
    with open("./keys.json", "r") as f:
        keys = json.load(f)


    host = "mail.privateemail.com"
    port = 465#TLS: 587; SSL: 465
    email = keys["email_address"]
    password = keys["email_password"]
    emailer = Emailer(host, port, email, password)
    msg = emailer.constructEmail("james@robinson.fyi", "TESTING", "TEST EMAIL", True)
    emailer.sendEmail(msg)

# %%
