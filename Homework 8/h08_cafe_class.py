# Author: Nate Goldsborough
# Assignment: Homework 8
# Filename: h08_cafe_class.py
# Class: INFOST350
# Date: 11/8/2021
# Description: This program will create a Cafe class that is a child of the Restaurant class, thn describe the cafe and its attributes, and display the menu.

from h08_restaurant_class import Restaurant as Rc

class Cafe(Rc):
    def __init__(self, name, type, menu):
        self.menu = menu
        super().__init__(name, type)
    
    def displayMenu(self):
        print("\nCafe Menu:")
        for item in self.menu:
            print(item)


def main():
    menu = ["Coffee", "Tea", "Cake", "Cookie", "Sandwich", "Pizza", "Burger", "Fries", "Salad", "Soup"]
    cafe = Cafe("muffin Hause", "Cafe", menu)
    cafe.describeRestaurant()
    cafe.openRestaurant()
    cafe.displayMenu()

if __name__ == "__main__":
    main()


# Sample Output:
# muffin Hause restaurant is a Cafe type of restaurant
# muffin Hause restaurant is open

# Cafe Menu:
# Coffee
# Tea
# Cake
# Cookie
# Sandwich
# Pizza
# Burger
# Fries
# Salad
# Soup