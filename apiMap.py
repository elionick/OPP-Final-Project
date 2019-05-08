import requests
import urllib
import sendEmail
import time


class maps():
    def __init__(self, address):
        self.key = "AIzaSyCGmcaD0lKJaFYRgU0nyBaHjQ1JX8r3A_o"
        self.location = ""
        self.destination = ""
        self.destinationaddress = ""
        self.type = ""
        self.directions = []
        self.polyline = ""
        self.address = address
        self.mode = ""

    def getLocation(self):
        main_api = "https://maps.googleapis.com/maps/api/geocode/json?"
        # address = input("Address: ")

        url = main_api + urllib.parse.urlencode({"address": self.address, "key": self.key})
        json_data = requests.get(url).json()

        json_status = json_data["status"]
        if json_status == "OK":
            for each in json_data["results"]:
                self.location = str(each["geometry"]["location"]["lat"]) + \
                    "," + str(each["geometry"]["location"]["lng"])
            return True

    def getImg(self):
        main_api = "https://maps.googleapis.com/maps/api/staticmap?"
        url = main_api + urllib.parse.urlencode({"center": self.location, "zoom": "14", "size": "640x640",
                                                 "scale": "2", "path": "color:0x0000ff80|weight:5|enc:"+self.polyline, "markers":"color:blue|" +self.location +"|" +self.destinationaddress, "key": self.key})

        r = requests.get(url)
        with open("map.png", "wb") as f:
            f.write(r.content)
            print("Map saved as map.png in your directory!")

    def getDirection(self):
        main_api = "https://maps.googleapis.com/maps/api/directions/json?"



        url = main_api + urllib.parse.urlencode({"origin": self.location, "key": self.key,
                                                 "destination": self.destination, "mode": self.mode, "departure_time": "now", "language": "en"})

        json_data = requests.get(url).json()
        json_status = json_data["status"]

        if json_status == "OK":
            polyline = json_data["routes"][0]["overview_polyline"]["points"]
            self.polyline = polyline

            for each in json_data["routes"][0]["legs"][0]["steps"]:
                self.directions.append(
                    [each["html_instructions"], each["distance"]["text"], each["duration"]["text"]])

    def getNearbyPlace(self, place):
        main_api = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

        if place == "supermarket":
            self.type = "supermarket"
            place = ""

        if place == "gym":
            self.type = "gym"
            place = ""

        url = main_api + urllib.parse.urlencode({"keyword": place, "key": self.key,
                                                 "location": self.location, "rankby": "distance", "type": self.type})
        json_data = requests.get(url).json()
        json_status = json_data["status"]

        if json_status == "OK":
            print("There are these places next to you: ")
            print()
            print()
            time.sleep(2)
            i = 0
            for each in json_data["results"]:
                print("Place Number: " + str(i))
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
        else:
            print("Error: Something went wrong with the mapAPI!")

    def getDistance(self):
        main_api = "https://maps.googleapis.com/maps/api/distancematrix/json?"

        url = main_api + urllib.parse.urlencode({"origins": self.location, "key": self.key,
                                                 "destinations": self.destination, "mode": self.mode, "departure_time": "now"})

        json_data = requests.get(url).json()
        json_status = json_data["status"]

        if json_status == "OK":
            origin = json_data["origin_addresses"][0]
            self.destinationaddress = json_data["destination_addresses"][0]
            distance = json_data["rows"][0]["elements"][0]["distance"]["text"]
            duration = json_data["rows"][0]["elements"][0]["duration"]["text"]

            print("Route calculated!")
            print()

            print("Your route:\n\n" + str(origin)+" to " + str(self.destinationaddress) + "\nThe distance is %s. It takes %s to get there." % (distance, duration))
            print()

    def sendEmail(self, email):
        sendEmail.sendEmail(self.type, email, self.directions)
        print("We sent you an email to " + str(email) +
              " with the route description, as well as a map!")


if __name__ == "__main__":
    pass
    #map = maps("Dorfmatte 1204, 3113 Rubigen")
    #map.getLocation()
    #map.getNearbyPlace("supermarket")
    #map.getDistance()
    #map.getDirection()
    #map.getImg()
    # map.sendEmail("priestrix@gmail.com")
