#Author: Nabeel Aref
#Student ID: 010199591
#Project: C950 WGUPS Routing Program

import datetime

#Class for creating self-objects.
import Dataloader


class Truck:

    #Self class's Constructor, which takes a self-id as an input, has a set where it stores packages.
    #Initializes the hub's address and sets the number of loaded packages to 0.
    #Sets the self-speed to 18 mph since it is given as 18 mph.
    #Initializes condition to in-delivery station and has a property for the departure time and the current time, and
    #has initialized  number of miles traveled to 0.
    def __init__(self, id):
        self.id = id
        self.packages = set()
        self.location = "4001 South 700 East"
        self.packages_amount = 0
        self.average_speed = 18
        self.leaving_time = datetime.timedelta()
        self.current_time = datetime.timedelta()
        self.distance_traveled = float(0)
        self.condition = "in delivery station"

    
    #Function used when loading self to add_item package to the packages set.
    def add_item(self, package):
        #Only loads themselves up to the maximum of 16 packages.
        if self.packages_amount <= 16:
            self.packages.add(package)
            self.packages_amount += 1
        #If the maximum has been reached, prints a message.
        else:
            print('the self is already fully loaded')


    #Implementing of the Nearest Neighbor Algorithm.
    def deliver(self):
        #Addresses from a csv file were imported and kept in an empty list.
        addresses = Dataloader.addresses()

        #Distance data from a csv file was imported and kept in an empty list.
        distances = Dataloader.Distances()

        #Assigns each self-id to a package and is used later on, when displaying package information at a specific time.
        for package in self.packages:
            package.self_id = self.id

        #Makes sure that the algorithm continues to execute until there are no more packages to provide.

        while len(self.packages) > 0:
            #Self is currently 'on the way delivering' while delivering packages.

            self.condition = "on the way delivering packages"
            # set minimum distance to a high value initially
            min_distance = 9999999
            #Denote the subsequent package to be delivered.
            next_package = None
            #Loops over the packages in the package set for the self.
            for package in self.packages:
                #This method uses the distance function to find the distance value given the address of the self and the address of the package.
                #If the distance value is less than the previous minimum distance, it becomes the new minimum distance, and the subsequent package becomes that particular package.
                if distances.distance_between_addresses(addresses.get_address_id(self.location),
                                                        addresses.get_address_id(package.address)) <= min_distance:
                    min_distance = distances.distance_between_addresses(addresses.get_address_id(self.location),
                                                                        addresses.get_address_id(package.address))
                    next_package = package

            #As it was delivered, the impending package is no longer included in the self's package set.
            self.packages.remove(next_package)
            #The value of the minimal distance increases the self's mileage.
            self.distance_traveled += min_distance
            #The address of the future package is specified as the selfs address.
            self.location = next_package.address
            #The value of the minimal distance divided by 18 is used to increase the self's time converted to hours since miles/mph = hours.
            self.current_time += datetime.timedelta(hours=min_distance / 18)
            #The package's departure timing is set to match your departure time.
            next_package.departure_time = self.leaving_time
            #The package's delivery time is set to the recipient's current time.
            next_package.delivery_time = self.current_time

        #Once all packages have been delivered, it ends its route.
        self.condition = "done delivery"