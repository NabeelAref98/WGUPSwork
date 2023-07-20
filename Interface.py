#Author: Nabeel Aref
#Student ID: 010199591
#Project: C950 WGUPS Routing Program

import datetime


# this class is the interface class, it deals with viewing the information details of the trucks and the packages
class Interface:
    def __init__(self, miles, packages):
        # the class starts here if loaded

        # supplies class variables with the given argument class variables
        self.miles = miles
        self.packages = packages

        # prints the emblem or company logo
        self.print_emblem()

        # starts the program functionality
        self.program_main_loop()

    # this functions prints the program functionality
    def print_emblem(self):
        print("*" * 50)
        print("*                      WGUPS                     *")
        print("*" * 50)

#change comments
    def all_packages(self):
        hour_input = input("Please enter an hour value between 0 and 23: ")
        if int(hour_input) >= 0 and int(hour_input) < 24:
            minute_input = input("Please enter a minute value between 0 and 59: ")
            if int(minute_input) >= 0 and int(minute_input) < 60:
                #Generates time input from hour and minute value.
                given_time = datetime.timedelta(hours=int(hour_input), minutes=int(minute_input))
            #Verifies minute value input.
            else:
                print("Invalid minute value entered.")
        #Confirms if valid hour value was entered.
        else:
            print("Invalid hour value entered.")
        for row in range(1, 41):
            package = self.packages.get_package_line(row)
            #The package condition is updated based on the time input, and a function from the package class is used.
            package.print_details(given_time)

    def single_packages(self):
        hour_input = input("Please enter an hour value between 0 and 23: ")
        #Confirms if valid hour value was entered.
        if int(hour_input) >= 0 and int(hour_input) < 24:
            minute_input = input("Please enter a minute value between 0 and 59: ")
            #Confirms if valid minute value was entered.
            if int(minute_input) >= 0 and int(minute_input) < 60:
                #Generates time input from hour and minute values.
                given_time = datetime.timedelta(hours=int(hour_input), minutes=int(minute_input))
            #If an invalid minute value is entered, an error notice is displayed and the application is terminated.
            else:
                print("Invalid minute value entered.")
        #If an improper hour value is entered, an error notice is displayed and the application is terminated.
        else:
            print("Invalid hour value entered.")
        #Asks the user to enter a package id between 1 and 40.
        package_id_input = input("Please enter a package id number between 1 and 40: ")

        #Confirms if valid package id was entered.
        if int(package_id_input) >= 1 and int(package_id_input) <= 40:
            #Based on the id entered by the user, retrieves a package from a hashtable.
            package = self.packages.get_package_line(int(package_id_input))
            package.print_details(given_time)

    #Prints all miles the trucks drove combined.
    def print_milage(self):
        print("\n\nThe total mileage for all 3 trucks is " + str(self.miles) + " miles\n\n")

    #The function will continue to loop until the user tells it to stop.
    def program_main_loop(self):
        #Sets run variable to true while the program is still running
        self.run = True
        while self.run:

            #Obtains the user's input option.
            menu_input = input(
                "choose a number options:\n[1] To get_item the condition of all packages at a given time \n[2] To "
                "get_item the condition of an individual package\n[3] print the mileage for all trucks\n[4] Quit\n>> ")

            #If user chooses 1 then they want all packages, then prints all packages.
            if (menu_input == '1'):
                self.all_packages()

            # if user chooses 2 then they want a certain package
            elif (menu_input == '2'):
                # prints a certain package of choice later will be asked to proide package id
                self.single_packages()

            # prints the total miles of the trucks
            elif (menu_input == '3'):
                self.print_milage()

            # if choosen 4 then the program exits
            elif (menu_input == '4'):
                self.run = False
            else:
                # prints an error message if an invalid option is choosen
                print("Invaild option please try again.\n")
