def get_file_lines(filename):
    file_lines = open(filename, "r").read()
    return file_lines
print(get_file_lines("poem.txt"))

print(" ")

def lines_printed_backwards(line_list):
    poem_dict_lines = open(line_list, "r").readlines()
    reverse = ''
    count = len(line_list)
    for line in poem_dict_lines:
        count = count - 1
        reverse = str(count) + " " + line
    return reverse
print(lines_printed_backwards("poem.txt"))
"""
the lines of the poem in reverse. 
Include the original line number at the beginning of each line.
"""
