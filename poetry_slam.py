def get_file_lines(filename):
    """
    Reaturns a list of strings containing the lines of the file
    """
    file_lines = open(filename, "r")
    poem_lines = file_lines.read().splitlines()
    file_lines.close()
    return poem_lines
    
print(get_file_lines("poem.txt"))

print(" ")

def lines_printed_backwards(filename):
    """
    The lines of the poem in reverse. 
    Include the original number at the beginning of each line
    """
    f = open(filename, 'r')
    line_list = f.read().splitlines()
    line_num = len(line_list)
    line_list = line_list[::-1]

    for i in range(len(line_list)):
        reverse = str(line_num - i) + " " + line_list[i]
        print(reverse)

lines_printed_backwards("./poem.txt")
