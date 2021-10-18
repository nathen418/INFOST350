# Author: Nate Goldsborough
# Assignment: Homework 5
# Filename: h06_miles_to-kilometers.py
# Class: INFOST350
# Date: 10/18/2021
# Description: This program converts miles to kilometers

def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

def main():
    try:
        miles = float(input("Enter the number of miles: "))
    except (ValueError, TypeError):
        print("You did not enter a number")
        main()
    kilometers = miles_to_kilometers(miles)
    print("The number of kilometers is: ", kilometers)

if __name__ == "__main__":
    main()

# Sample Output:
# Enter the number of miles: 60
# The number of kilometers is:  96.5604