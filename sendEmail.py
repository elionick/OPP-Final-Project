import smtplib
from email.message import EmailMessage


def sendEmail():

    subjects = {"Gym": "Here is a map to your nearest gym!",
                "Supermarket": "Here is a map to your nearest Supermarket!",
                "Shoppinglist": "Here is your shopping list!"
                }

    msg = EmailMessage()
    msg["Subject"] = subjects["Supermarket"]
    msg["From"] = "oopfitness19@gmail.com"
    msg["To"] = "priestrix@gmail.com"
    msg.set_content("This should resemble a route description.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("oopfitness19@gmail.com", "357rp/5<RQ}.('R?")
        smtp.send_message(msg)
