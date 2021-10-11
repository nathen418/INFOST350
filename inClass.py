# Author: Nate Goldsborough
# Assignment: Homework 4
# Filename: h04_used_cars.py
# Class: INFOST350
# Date: 10/4/2021
# Description: Understand how to use dictionaries and lists and how to loop thru them easily

class Car:
    def __init__(self, owner_lname, owner_fname, model_name, brand, price_list):
        self.owner_lname = owner_lname
        self.owner_fname = owner_fname
        self.model_name = model_name
        self.brand = brand
        self.price_list = price_list
        return {'owner_lname': self.owner_lname, 'owner_fname': self.owner_fname, 'model_name': self.model_name, 'brand': self.brand, 'price_list': self.price_list}

def main():
    tesla_modelS = Car('Goldsborough', 'Nate', 'Model S', 'Tesla', '$1,000,000')
    used_cars = [tesla_modelS]
    for car in used_cars:
        for key, value in car.items():
            print(f'{key}: {value}')
        print('\n')
    
if __name__ == '__main__':
    main()

# Sample Output:
# owner_lname: tommas
# owner_fname: harry
# model_name: modelS
# brand: tesla
# price_list: 13500.0


# owner_lname: Carlyle
# owner_fname: London
# model_name: Civic
# brand: Honda
# price_list: 21000.0


# owner_lname: Robinson
# owner_fname: sam
# model_name: Altima
# brand: Nisan
# price_list: 24000.0

