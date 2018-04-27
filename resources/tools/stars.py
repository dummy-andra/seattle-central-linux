#!/bin/python
import os
'''
A program which takes in a command line argument and outputs the result with
stars at the first and last index.
'''


def stars(string):
    print('*' + string.replace('\n', '') + '*')


# TODO: make it work with sysarg
# import sys
print("please modify the file ~/questions with your questions to star!")

file = open("questions.txt", "r")

file_lines = file.readlines()
for line in file_lines:
    if len(line) > 1:
        stars(line)
    else:
        print('')


# if __name__ == "__main__":
#     # if invoked as main program, parse arguments
#     string = str(sys.argv[1:]).join(" ")
#     print('*' + string + '*')
