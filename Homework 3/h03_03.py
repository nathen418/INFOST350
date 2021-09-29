# Author: Nate Goldsborough
# Assignment: Homework 3
# Filename: h03_03.py
# Class: INFOST350
# Date: 9/29/2021
# Description: This program demonstrates an understanding of how to modify lists and how index values operate.

def main():
    cars = ['accord', 'acura', 'lexus', 'audi', 'jaguar', 'peugeot', 'GMC']

    # remove the unwanted elements of the list, cars
    cars.pop(0) 
    cars.pop(4)
    cars.pop(4)

    # print the list
    print(cars) 
    
if __name__ == '__main__':
    main()

# Sample Output
# ['acura', 'lexus', 'audi', 'jaguar']