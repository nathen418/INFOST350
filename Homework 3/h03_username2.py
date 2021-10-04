# Author: Nate Goldsborough
# Assignment: Homework 3
# Filename: h03_int_remainder.py
# Class: INFOST350
# Date: 9/29/2021
# Description: This program creates a username based on some input data

# generate usernames using the user’s first initial,
#  followed by the initial of user’s middle name, and up to 4 letters of the user’s last name.  

def main():
	print("This program generates computer user names. \n")

	#get user’s first name and last names
	first = input("Please enter your first name: ")
	middle = input("Please enter your middle name: ")
	last = input("Please enter your last name: ")


	# concatenate first initial with 3 chars of the last name.
	uname = first.lower()[0] + middle.lower()[0] + last.lower()[ :4]

	#output the username
	print("Your username is: ", uname)

if __name__ == "__main__":
	main()

# Sample Output:
# Please enter your first name: Nate
# Please enter your middle name: Clay
# Please enter your last name: Goldsborough
# Your username is: ncgold