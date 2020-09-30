#importing random(). This allows us to get a random selection of things
from random import randint

print(" ") #Adding a space between the functions in the terminal

# FUNCTION 1----------------------------------------------------
def get_file_lines(filename):
    """
    Reaturns a list of strings containing the lines of the file
    """
    file_lines = open(filename, "r")
    poem_lines = file_lines.read().splitlines()
    file_lines.close()
    return poem_lines

print(get_file_lines("./poem1.txt"))

print(" ") #Adding a space between the functions in the terminal

# FUNCTION 2----------------------------------------------------
def lines_printed_backwards(line_list):
    """
    The lines of the poem will be printed in reverse order. 
    Includes the original number at the beginning of each line
    """
    line_list = line_list[::-1]
    line_num = len(line_list)

    for i in range(line_num):
        reverse = str(line_num - i) + " " + line_list[i]
        print(reverse)

poem = open('./poem1.txt', 'r')
lines_printed_backwards(poem.read().splitlines())

print(" ")#Adding a space between the functions in the terminal

# FUNCTION 3----------------------------------------------------
def lines_printed_random(line_list):
    """
    The lines of the poem will be printed in a random order.
    """
    line_num = len(line_list)
    for i in range(line_num):
        rand = line_list[randint(i, line_num-1)]
        print(rand)

poem = open('./poem1.txt', 'r')
lines_printed_random(poem.read().splitlines())

print(" ")#Adding a space between the functions in the terminal

# FUNCTION 4----------------------------------------------------
def lines_printed_custom(line_list):
    """
    The lines of the poem will be printed in a alphabetical order.
    """
    #sorted function return a sorted alchabetically ordered list.
    # Here, we are reversing the alphabetical sort with reverse=True. 
    # So, it will return a descending alphabetically orded list
    for line in sorted(line_list, reverse=True):
        #end='' will end the line with a space
        print(line, end='')
poem = open('./poem1.txt', 'r')
lines_printed_custom(poem.readlines())