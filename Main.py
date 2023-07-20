#Author: Nabeel Aref
#Student ID: 010199591
#Project: C950 WGUPS Routing Program

import Interface
import Dataloader

#Loads all of the packages.
packages = Dataloader.Packages()

#Get all trucks to deliver their goods.
total_combined_mileage = Dataloader.setup_trucks(packages)

#Supplies the user with a user interface.
Interface.Interface(total_combined_mileage, packages)

