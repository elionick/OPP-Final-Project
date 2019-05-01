import smtplib
from email.message import EmailMessage




def sendEmail(topic, receiver, directions):

    subjects = {"gym": "Here is a map to your desired gym!",
                "supermarket": "Here is a map to your desired supermarket!",
                "shoppinglist": "Here is your shopping list!"
                }

    messages = {"gym" : "This is the route description to your desired gym.\nPlease find attached the route on the map!\n",
                "supermarket": "This is the route description to your desired supermarket.\nPlease find attached the route on the map!\n",
                "shoppinglist": "This is your shopping list: "}

    msg = EmailMessage()
    msg["Subject"] = subjects[topic]
    msg["From"] = "oopfitness19@gmail.com"
    msg["To"] = receiver

    if topic == "gym" or topic == "supermarket":
        directionList = []

        # Construct the email in HTML
        directionList.append("<DOCTYPE HTML!>\n<html>\n<body>")
        directionList.append("<h1>" +messages[topic] +"</h1>")
        for i in range(len(directions)):
            directionList.append((str(i+1) + ". " + directions[i][0] + " (" + str(directions[i][1]) + " / " + str(directions[i][2]) + ")"))
        directionList.append("</body>\n</html>")
        directions_joined = "<br>".join(directionList)

        msg.set_content(messages[topic] +"\n" +str(directions_joined))
        msg.add_alternative(directions_joined, subtype="html")

    else:
        msg.set_content(messages[topic])

    with open("map.png", "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("oopfitness19@gmail.com", "357rp/5<RQ}.('R?")
        smtp.send_message(msg)



if __name__ == "__main__":
    pass
    #directions = [['Head <b>northwest</b> on <b>Geltenwilenstrasse</b> toward <b>Unterstrasse</b>', '0.2 km', '3 mins'], ['Turn <b>right</b> onto <b>Vadianstrasse</b>', '0.7 km', '9 mins'], ['Turn <b>right</b> onto <b>Multertor</b>', '18 m', '1 min'], ['<b>Multertor</b> turns slightly <b>left</b> and becomes <b>Multergasse</b>', '0.2 km', '2 mins'], ['Slight <b>right</b> onto <b>Bärenpl.</b>', '16 m', '1 min'], ['Continue onto <b>Spisergasse</b>', '55 m', '1 min'], ['Turn <b>left</b> onto <b>Kugelgasse</b>', '51 m', '1 min'], ['Turn <b>right</b> onto <b>Löwengasse</b>', '57 m', '1 min']]
    #sendEmail("supermarket", "priestrix@gmail.com", directions)