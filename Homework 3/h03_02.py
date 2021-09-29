# Author: Nate Goldsborough
# Assignment: Homework 3
# Filename: h03_02.py
# Class: INFOST350
# Date: 9/29/2021
# Description: prints parts and whole versions of tuples, and attempts to change them. Also explains nested lists/tuples

def main():
    my_tuple = ('c','l','a','s','s','350', 'fall', '2021')
    n_tuple = ("tuple", [3, 4, 6], (1, 5, 3))
    print(my_tuple[5]) # prints the value: 350
    print(n_tuple[:]) # prints whole tuple
    try:
        my_tuple.pop(6) # throws an error because tuples are immutable
    except(AttributeError):
        print("That is an immutable object")
    print(n_tuple[1][2]) # prints 6 because n_tuple is a tuple of lists, and the second element in n_tuple is a list of 3 ints, and the third int is 6

if __name__ == "__main__":
    main()

# Sample Output:
# 350
# ('tuple', [3, 4, 6], (1, 5, 3))
# That is an immutable object6