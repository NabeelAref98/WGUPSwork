#Author: Nabeel Aref
#Student ID: 010199591
#Project: C950 WGUPS Routing Program


import csv
from Hashtable import *
from Package import *
from Truck import Truck


#Depending on the request, this class loads all of the csv address lines and returns them.
class addresses:
    def __init__(self):
        # the function loads first in the class

        #The address in this class list variable is returned by the function that loads first in the class.
        self.allAddresses = []
        #Returns the file handle after retrieving the file.
        addressFile = open('Addresses.csv')
        #Begins reading values from the address file before splitting them.
        csvObject = csv.reader(addressFile, delimiter=',')
        #The address is added to the list.
        for row in csvObject:
            self.allAddresses.append(row)

    #Obtains the desired address's address id.
    def get_address_id(self, address_input):
        for row in self.allAddresses:
            #If the row resembles the input, the address must be correct.
            if address_input == row[2]:
                #Returns the address.
                return int(row[0])

    # Returns all addresses (loaded and available).
    def get_all_addreses(self):
        return self.allAddresses


class Distances:
    def __init__(self):
        #The function loads the class.

        #Returns the file handle and opens the file
        distanceFile = open('Distances.csv')
        # reads the csv file
        csvObject = csv.reader(distanceFile, delimiter=',')
        # gets the list object of the csv file value and stores it in the class variable
        self.distances = list(csvObject)

    # this function finds the distance between two address
    def distance_between_addresses(self, address_id1, address_id2):
        # retrieves the value from the csv line in the list
        distance_value = self.distances[address_id1][address_id2]
        if distance_value != '':
            # if there a no value retrieve it again just in case
            distance_value = self.distances[address_id1][address_id2]
        else:
            # this is a error fix, there must be a switch up between the parameter order
            distance_value = self.distances[address_id2][address_id1]
        # returns the distance in float to support non-full number values
        return float(distance_value)

    # returns the list of all the distances
    def get_all_distances(self):
        return self.distances


# this is the class that returns all the packages
class Packages:
    def __init__(self):
        # the function loads first in the class

        # creates a hash table to load the packages in
        self.packages = Hashtable()

        # opens the file an returns the handle for the file
        package_csvfile = open('Packages.csv')
        # reads the csv lines
        csvObject = csv.reader(package_csvfile, delimiter=',')
        # reads the property of csv object to put it into a class package object
        for row in csvObject:
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            postal_code = row[4]
            deadline = row[5]
            weight = row[6]
            # because object is just being created likely its still not delivered
            condition = "in delivery station"
            # creates the object
            package = Package(id, address, city, state, postal_code, deadline, weight, condition)
            # adds the package object
            self.packages.add_item(id, package)

    # returns a all packages hashtable
    def get_all_packages(self):
        return self.packages

    # returns only a line if given
    def get_package_line(self, line):
        return self.packages.get_item(line)


def setup_trucks(packages):
    #This method depicts loading each truck by using a 'for loop' to add item packages with the listed ids into the truck's package collection.
    #Uses add_item function from the 'Truck' class
    truck1 = Truck(1)
    for row in [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]:
        truck1.add_item(packages.get_package_line(row))

    truck2 = Truck(2)
    for row in [3, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]:
        truck2.add_item(packages.get_package_line(row))

    truck3 = Truck(3)
    for row in [6, 2, 4, 5, 7, 8, 10, 11, 25, 28, 32, 33]:
        truck3.add_item(packages.get_package_line(row))

    #Set the departure and current times to times determined by the packages.
    #Truck 1 will be the first to leave at 8, which will help accommodate for certain package deadlines.
    #Due to an address issue with package 9, truck 2 will depart at 10:20.
    #Truck 3 will leave at 9:05 to account for the delayed packages. All other packages do not have a deadline.

    truck1.leaving_time = datetime.timedelta(hours=8)
    truck1.current_time = datetime.timedelta(hours=8)
    truck2.leaving_time = datetime.timedelta(hours=10, minutes=20)
    truck2.current_time = datetime.timedelta(hours=10, minutes=20)
    truck3.leaving_time = datetime.timedelta(hours=9, minutes=5)
    truck3.current_time = datetime.timedelta(hours=9, minutes=5)

    #For each truck, the Nearest-Neighbor delivery algorithm is used.
    truck1.deliver()
    truck2.deliver()
    #Because there are only two drivers, the algorithm is only run if truck 1 or truck 2 has completed their route.
    if truck1.condition == "done delivery" or truck2.condition == "done delivery":
        truck3.deliver()

    #Total mileage is calculated by summing the mileage of each truck.
    return truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled