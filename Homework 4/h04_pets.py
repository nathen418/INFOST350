# Author: Nate Goldsborough
# Assignment: Homework 4
# Filename: h04_pets.py
# Class: INFOST350
# Date: 10/4/2021
# Description: Remove all instances of 'rat' from a list of pets
def main():
    pets = ['dog', 'rat', 'rat', 'fish', 'cat', 'rat', 'dog', 'goldfish', 'rat', 'cat', 'cat', 'rabbit', 'fish', 'rat']
    while ('rat' in pets):
        pets.remove('rat')
    print(pets)


if __name__ == '__main__':
    main()

# Sample Output:
# ['dog', 'fish', 'cat', 'dog', 'goldfish', 'cat', 'cat', 'rabbit', 'fish']