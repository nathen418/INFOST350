# Author: Nate Goldsborough
# Assignment: Homework 4
# Filename: h04_months.py
# Class: INFOST350
# Date: 10/4/2021
# Description: print out 2 lists at the same time

def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in range(len(months)):
        print(months[i], numbers[i], end='  ')


if __name__ == "__main__":
    main()

# Sample Output:
# January 1  February 2  March 3  April 4  May 5  June 6  July 7  August 8  September 9  October 10  November 11  December 12