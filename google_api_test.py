import urllib
import requests


def getPlace():
    main_api = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

    while True:
        place = input("Do you want to find a supermarket or gym? (s/g) ")

        if place == "quit" or place == "q":
            print("goodbye, have fun coding")
            break

        url = main_api + urllib.parse.urlencode({"input": place, "key": "AIzaSyCGmcaD0lKJaFYRgU0nyBaHjQ1JX8r3A_o", "inputtype": "textquery", "fields": "opening_hours,formatted_address,geometry,user_ratings_total"})
        print(url)

        json_data = requests.get(url).json()
        json_status = json_data["status"]
        print("API Status: " + json_status)
        print("----------------------------------------------")

        if json_status == "OK":
            for each in json_data["candidates"]:
                print(each["formatted_address"])
                print("Open now: " + str(each["opening_hours"]["open_now"]))
                print("----------------------------------------------")



def getNearbyPlace():
    main_api = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    while True:
        place = input("Do you want to find a supermarket or gym? (s/g) ")
        type = ""

        if place == "quit" or place == "q":
            print("goodbye, have fun coding")
            break

        if place == "s":
            type = "supermarket"
            place = ""

        if place == "g":
            type = "gym"
            place = ""

        url = main_api + urllib.parse.urlencode(
            {"keyword": place, "key": "AIzaSyCGmcaD0lKJaFYRgU0nyBaHjQ1JX8r3A_o", "location": "47.429889,9.376306","rankby": "distance", "opennow": "", "type":type})
        print(url)

        json_data = requests.get(url).json()
        json_status = json_data["status"]
        print("API Status: " + json_status)
        print("----------------------------------------------")

        if json_status == "OK":
            for each in json_data["results"]:
                print("Name: " +str(each["name"]))
                print("Place-Id: " + str(each["place_id"]))
                print("Adress: " + str(each["vicinity"]))
                if each["opening_hours"]["open_now"]:
                    print("Open now: " + str(each["opening_hours"]["open_now"]))

                print("----------------------------------------------")


def getDistance():
    main_api = "https://maps.googleapis.com/maps/api/distancematrix/json?"

    while True:

        mode = input("How do you want to go there? (walking/transit/driving) ")

        if mode == "quit" or mode == "q":
            print("goodbye, have fun coding")
            break

        url = main_api + urllib.parse.urlencode({"origins": "47.429889,9.376306", "key": "AIzaSyCGmcaD0lKJaFYRgU0nyBaHjQ1JX8r3A_o",
                                                 "destinations": "place_id:ChIJa04EtIwem0cRZW_G-OOE9zo", "mode": mode, "departure_time":"now"})
        print(url)

        json_data = requests.get(url).json()
        json_status = json_data["status"]
        print("API Status: " + json_status)
        print("----------------------------------------------")

        if json_status == "OK":
            origin = json_data["origin_addresses"][0]
            destination = json_data["destination_addresses"][0]
            distance = json_data["rows"][0]["elements"][0]["distance"]["text"]
            duration = json_data["rows"][0]["elements"][0]["duration"]["text"]
            print("From "+str(origin)+" to " +str(destination) + "it is %s and takes %s" %(distance,duration))
            print("----------------------------------------------")





def getLocation():
    main_api = "https://maps.googleapis.com/maps/api/geocode/json?"

    while True:
        address = input("Address: ")
        if address == "quit" or address == "q":
            print("goodbye, have fun coding")
            break
        url = main_api + urllib.parse.urlencode({"address": address, "key": "AIzaSyCGmcaD0lKJaFYRgU0nyBaHjQ1JX8r3A_o"})
        print(url)

        json_data = requests.get(url).json()
        json_status = json_data["status"]
        print("API Status: " + json_status)

        if json_status == "OK":
            for each in json_data["results"][0]["address_components"]:
                print(each["long_name"])
            if json_data["results"][0]["formatted_address"]:
                formatted_address = json_data["results"][0]["formatted_address"]
                print()
                print(formatted_address)




if __name__ == '__main__':
    getDistance()
    #getNearbyPlace()

