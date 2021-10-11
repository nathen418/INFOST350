# Author: Nate Goldsborough
# Assignment: Homework 4
# Filename: h04_used_cars.py
# Class: INFOST350
# Date: 10/4/2021
# Description: Understand how to use dictionaries and lists and how to loop thru them easily

def main():
    tesla_modelS = {'owner_lname': 'tommas', 'owner_fname': 'harry', 'model_name': 'modelS', 'brand': 'tesla', 'price_list': 13500.00}
    hondaCivic = {'owner_lname': 'Carlyle', 'owner_fname': 'London', 'model_name': 'Civic', 'brand': 'Honda', 'price_list': 21000.00}
    nisanAltima = {'owner_lname': 'Robinson', 'owner_fname': 'sam', 'model_name': 'Altima', 'brand': 'Nisan', 'price_list': 24000.00}
    used_cars = [tesla_modelS, hondaCivic, nisanAltima]
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

