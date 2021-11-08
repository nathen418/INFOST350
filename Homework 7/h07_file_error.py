# Author: Nate Goldsborough
# Assignment: Homework 7
# Filename: h07_file_error.py
# Class: INFOST350
# Date: 10/25/2021
# Description: This program will read in a file and count the number of words in the file.

def main():
    filenames = ['anna.txt', 'gatsby.txt', 'don_quixote.txt', 'beloved.txt', 'mockingbird.txt']
    for name in filenames:
        try:
            with open(name, 'r') as f:
                print(f'The file {name} has {len(f.read().split())} words.')
        except FileNotFoundError:
            print(f'{name} not found')
if __name__ == '__main__':
    main()

# Sample Output:
# The file anna.txt has 168 words.
# gatsby.txt not found
# The file don_quixote.txt has 146 words.
# The file beloved.txt has 127 words.
# mockingbird.txt not found