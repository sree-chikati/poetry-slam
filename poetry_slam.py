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

def lines_printed_backwards(line_list):
    """
    The lines of the poem in reverse. 
    Include the original number at the beginning of each line
    """
    line_list = line_list[::-1]
    line_num = len(line_list)

    for i in range(len(line_list)):
        reverse = str(line_num - i) + " " + line_list[i]
        print(reverse)

poem = open('./poem.txt', 'r')
lines_printed_backwards(poem.read().splitlines())

def lines_printed_random(line_list):
    return
