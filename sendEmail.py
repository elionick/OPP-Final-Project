import smtplib
from email.message import EmailMessage




def sendEmail(topic, receiver, content):

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
        for i in range(len(content)):
            directionList.append((str(i+1) + ". " + content[i][0] + " (" + str(content[i][1]) + " / " + str(content[i][2]) + ")"))
        directionList.append("</body>\n</html>")
        directions_joined = "<br>".join(directionList)

        msg.set_content(messages[topic] +"\n" +str(directions_joined))
        msg.add_alternative(directions_joined, subtype="html")

        with open("map.png", "rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

    if topic == "shoppinglist":
        shoppinglistresult = []

        # Construct the email in HTML
        shoppinglistresult.append("<DOCTYPE HTML!>\n<html>\n<body>")
        shoppinglistresult.append("<h1>" + messages[topic] + "</h1>")
        for i in range(len(content)):
            shoppinglistresult.append((content[i]))
        shoppinglistresult.append("</body>\n</html>")
        shopping_joined = "<br>".join(shoppinglistresult)

        msg.set_content(messages[topic] + "\n" + str(shopping_joined))
        msg.add_alternative(shopping_joined, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("oopfitness19@gmail.com", "357rp/5<RQ}.('R?")
        smtp.send_message(msg)



if __name__ == "__main__":
    pass