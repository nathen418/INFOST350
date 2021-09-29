# Author: Nate Goldsborough
# Assignment: Homework 2
# Filename: h01_01.py
# Class: INFOST350
# Date: 9/25/2021
# Description: This program creates a list and then modifies it, while printing the list each time


fruit = ["Apple", "Orange", "Cherry", "Peach", "Strawberry", "Plum", "Grapes"]
print(fruit)

fruit.append("Guava")
fruit.append("Mango")
fruit.append("Papaya")
print(fruit)

fruit.pop(-1)
print(fruit)

fruit.pop(-2)
print(fruit)

# Sample Output:
# ['Apple', 'Orange', 'Cherry', 'Peach', 'Strawberry', 'Plum', 'Grapes']
# ['Apple', 'Orange', 'Cherry', 'Peach', 'Strawberry', 'Plum', 'Grapes', 'Guava', 'Mango', 'Papaya']
# ['Apple', 'Orange', 'Cherry', 'Peach', 'Strawberry', 'Plum', 'Grapes', 'Guava', 'Mango']
# ['Apple', 'Orange', 'Cherry', 'Peach', 'Strawberry', 'Plum', 'Grapes', 'Mango']