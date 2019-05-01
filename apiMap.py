import requests
import urllib
import sendEmail

class maps():
    def __init__(self):
        self.key = "AIzaSyCGmcaD0lKJaFYRgU0nyBaHjQ1JX8r3A_o"
        self.location = ""
        self.destination = ""
        self.type = ""
        self.directions = []
        self.polyline = ""

    def getImg(self):
        main_api = "https://maps.googleapis.com/maps/api/staticmap?"
        url = main_api + urllib.parse.urlencode({"center": self.location, "zoom":"14", "size":"640x640", "scale":"2", "path": "color:0x0000ff80|weight:5|enc:"+self.polyline, "key": self.key})

        r = requests.get(url)
        with open("map.png", "wb") as f:
            f.write(r.content)
            print("Map saved as map.png in your directory!")

    def getDirection(self):
        main_api = "https://maps.googleapis.com/maps/api/directions/json?"

        url = main_api + urllib.parse.urlencode({"origin": self.location, "key": self.key,
             "destination": self.destination, "mode": "walking", "departure_time": "now", "language": "en"})

        print(url)

        json_data = requests.get(url).json()
        json_status = json_data["status"]
        print("API Status: " + json_status)
        print("----------------------------------------------")

        if json_status == "OK":
            polyline = json_data["routes"][0]["overview_polyline"]["points"]
            self.polyline = polyline
            print("----------------------------------------------")
            for each in json_data["routes"][0]["legs"][0]["steps"]:
                self.directions.append([each["html_instructions"], each["distance"]["text"], each["duration"]["text"]])

            print("Route created!")
            print("----------------------------------------------")


    def getNearbyPlace(self):
        main_api = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        place = input("Do you want to find a supermarket or gym? (s/g) ")

        if place == "quit" or place == "q":
            print("goodbye, have fun coding")

        if place == "s":
            self.type = "supermarket"
            place = ""

        if place == "g":
           self.type = "gym"
           place = ""

        url = main_api + urllib.parse.urlencode({"keyword": place, "key": self.key, "location": self.location, "rankby": "distance", "type": self.type})
        print(url)
        json_data = requests.get(url).json()
        json_status = json_data["status"]
        print("API Status: " + json_status)
        print("----------------------------------------------")

        if json_status == "OK":
            i = 0
            for each in json_data["results"]:
                print("Result Number: " + str(i))
                i += 1
                print("Name: " + str(each["name"]))
                print("Place-Id: " + str(each["place_id"]))
                print("Adress: " + str(each["vicinity"]))
                try:
                    if each["opening_hours"]["open_now"]:
                        print("Open now: " + str(each["opening_hours"]["open_now"]))
                except:
                    print("Not open now!")

                print("----------------------------------------------")
                print()

            decision = int(input("Where would you like to go? Pick the number of the place: "))
            self.destination = "place_id:" + str(json_data["results"][decision]["place_id"])


    def getLocation(self):
        main_api = "https://maps.googleapis.com/maps/api/geocode/json?"
        address = input("Address: ")

        url = main_api + urllib.parse.urlencode({"address": address, "key": self.key})
        json_data = requests.get(url).json()

        json_status = json_data["status"]
        print("API Status: " + json_status)

        if json_status == "OK":
            for each in json_data["results"]:
                self.location = str(each["geometry"]["location"]["lat"]) + "," + str(each["geometry"]["location"]["lng"])
                print(self.location)


    def getDistance(self):
        main_api = "https://maps.googleapis.com/maps/api/distancematrix/json?"


        url = main_api + urllib.parse.urlencode({"origins": self.location, "key": self.key,
                                                 "destinations": self.destination, "mode": "walking", "departure_time": "now"})

        json_data = requests.get(url).json()
        json_status = json_data["status"]
        print("API Status: " + json_status)
        print("----------------------------------------------")


        if json_status == "OK":
            origin = json_data["origin_addresses"][0]
            destination = json_data["destination_addresses"][0]
            distance = json_data["rows"][0]["elements"][0]["distance"]["text"]
            duration = json_data["rows"][0]["elements"][0]["duration"]["text"]
            print("From "+str(origin)+" to " + str(destination) +
                  " it is %s and takes %s" % (distance, duration))
            print("----------------------------------------------")

    def sendEmail(self):
        sendEmail.sendEmail(self.type, "priestrix@gmail.com", self.directions)
        print("We sent you an email with the route description, as well as a map!")


if __name__ == "__main__":

    map = maps()
    map.getLocation()
    map.getNearbyPlace()
    map.getDistance()
    map.getDirection()
    map.getImg()
    map.sendEmail()



