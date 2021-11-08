# Author: Nate Goldsborough
# Assignment: Homework 7
# Filename: h07_book.py
# Class: INFOST350
# Date: 10/25/2021
# Description: Write movie info to a file when a user inputs it

def main():
    cont = True
    while (cont):
        book = input("Enter the name of the book: ")
        author = input("Enter the name of the author: ")
        why = input("Why do you like this book? ")
        file = open("h07_movie.txt", "a")
        file.write("\n" + book + " by " + author + ": " + why)
        file.close()
        cont = input("Do you want to enter another book? (y/n) ")
        if (cont.lower() == "n"):
            cont = False
        else:
            cont = True

if __name__ == "__main__":
    main()

# Sample output:
# Enter the name of the book: Harry potter
# Enter the name of the author: JKR
# Why do you like this book? it has magic
# Do you want to enter another book? (y/n) y
# Enter the name of the book: Magic schoolbus
# Enter the name of the author: Joanna Cole and Bruce Degen.
# Why do you like this book? it was funny
# Do you want to enter another book? (y/n) n

# File:
# Harry potter by JKR: it has magic
# Magic schoolbus by Joanna Cole and Bruce Degen.: it was funny