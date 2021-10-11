# Author: Nate Goldsborough
# Assignment: Homework 5
# Filename: h05_registration_fees.py
# Class: INFOST350
# Date: 10/11/2021
# Description: Calculate the annual registration fees for vehicles

def main():
    fee = 0
    vehicle_type = input("What type of vehicle are you registering? (Car or Truck) ")
    vehicle_weight = float(input("What is the weight of the vehicle in pounds? "))
    if (vehicle_type.lower() == "car"):
        if (vehicle_weight < 3000):
            fee = 125
        elif (vehicle_weight >= 3000):
            fee = 200
    elif (vehicle_type.lower() == "truck"):
        if (vehicle_weight < 4000):
            fee = 250
        elif (vehicle_weight >= 4000):
            fee = 350
    print(f'The registration fee for this vehicle is ${str(fee)}.00')

if __name__ == "__main__":
    main()

# Sample Output:
# What type of vehicle are you registering? (Car or Truck) car
# What is the weight of the vehicle in pounds? 2500
# The registration fee for this vehicle is $125