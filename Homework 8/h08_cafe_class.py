# Author: Nate Goldsborough
# Assignment: Homework 8
# Filename: h08_resteraunt_class.py
# Class: INFOST350
# Date: 11/8/2021
# Description: 

import h08_restaurant_class as Rc

class Cafe(Rc):
    def __init__(self, name, type, menu):
        self.menu = menu
        super().__init__(name, type)
    
    def displayMenu(self):
        print("\nCafe Menu:")
        for item in self.menu:
            print(item)


def main():
    menu = ["Coffee", "Tea", "Cake"]
    cafe = Cafe("muffin Hause", "Cafe", menu)
    cafe.describeRestaurant()
    cafe.openRestaurant()
    cafe.displayMenu()

if __name__ == "__main__":
    main()
