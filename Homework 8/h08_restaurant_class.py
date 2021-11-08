# Author: Nate Goldsborough
# Assignment: Homework 8
# Filename: h08_resteraunt_class.py
# Class: INFOST350
# Date: 11/8/2021
# Description: Use classes to create resteraunt objects and use methods to describe and open them

class Restaurant:
    """This class creates an object of type Restaurant"""
    def __init__(self, name, rType):
        self.name = name
        self.type = rType
    
    def describeRestartant(self):
        print(f'{self.name} restaurant is a {self.type} type of restaurant')

    def openRestaurant(self):
        print(f'{self.name} restaurant is open')


def main():
    """This function creates an object of type Restaurant"""
    restaurants = [Restaurant('Pizza Hut', 'Pizza'), Restaurant('Ramen House', 'Ramen'), Restaurant('Whole Foods', 'Grocery Store')]

    for restaurant in restaurants:
        if restaurant.name == 'Pizza Hut':
            print(f'Raw data:\nType: {restaurant.type}\nName: {restaurant.name}')
        restaurant.describeRestartant()
        restaurant.openRestaurant()


if __name__ == "__main__":
    main()

        