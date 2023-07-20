#Author: Nabeel Aref
#Student ID: 010199591
#Project: C950 WGUPS Routing Program



#This class is used for producing package objects.
import datetime


class Package:
    #Object constructor for packages, includes every attribute from the packages' csv file.
    #Space-Time complexity O(1)
    def __init__(self, id, address, city, state, zip, deadline, weight, condition):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        #Used get_item to determine a package's condition.
        self.condition = condition
        #Used to identify and assign truck ID's to packages.
        #Confirms the package is on the appropiate truck.
        self.truck_id = None
        #Used get_item to obtain an item's departure timing for a shipment.
        self.departure_time = None
        #Used get_item to get the time of delivery for a package.
        self.delivery_time = None

    #Function to set a package's condition based on time input.
    def package_condition(self, given_time):
        #If the input time occurs after the delivery time, the package is delivered.
        if self.delivery_time< given_time :
            self.condition = "delivered"
        #If the input time comes after the departing time but before the delivery time, the parcel is on its way.
        elif   given_time < self.delivery_time and given_time > self.departure_time:
            self.condition = "on the way delivering packages"
        #If any other time is input, the package is at the hub.
        else:
            self.condition = "in delivery station"
    def print_details(self,given_time):
        self.package_condition(given_time)
        special_package_time = datetime.timedelta(hours=10, minutes=20)
        if self.id == 9 and given_time > special_package_time:self.address = "410 s state st"
        else:self.address = "300 state st"
        #Provides all of the specifications needed for each package.
        print("package id: " + str(self.id))
        print("truck id: " + str(self.truck_id))
        print("address: " + self.address)
        print("deadline: " + self.deadline)
        print("city: " + self.city)
        print("zipcode: " + self.zip)
        print("weight: " + self.weight)
        print("departure time: " + str(self.departure_time))
        print("condition: " + self.condition)
        #Only displays a delivery time when the package delivery has been confirmed.
        if self.condition == "delivered":
            print("delivery time: " + str(self.delivery_time) + "\n\n")
        else:
            print("\n\n")

