def get_file_lines(filename):
    """
    Reaturns a list of strings containing the lines of the file
    """
    f = open(filename, "r")
    poem_lines = f.read().splitlines()
    f.close()
    return poem_lines
    
print(get_file_lines("poem.txt"))

print(" ")

#def lines_printed_backwards(line_list):
#    """
#    The lines of the poem in reverse. 
#    Include the original number at the beginning of each line
#    """
#  