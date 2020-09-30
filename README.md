# Poetry-Slam
 CS 1.0 Assignment: Poetry Slam
 
 Create for functions with the following criteria:
 
   1. **get_file_lines()**:
      -  It should have 1 parameter called *filename*, which is a string of the filename.
      -  It should return a list of strings containing the lines of the file.
   
   2. **lines_printed_backwards()**:
      -  It should have 1 parameter called *lines_list*, which is a list of strings containing lines of your poem.
      -  It should print the lines of the poem in reverse. Include the original line number at the beginning of each line.
      
   3. **lines_printed_random()**:
      -  It should have 1 parameter called *lines_list*, which is a list of strings containing lines of your poem.
      -  It should print the lines of your poem in randomly order. Repeats are ok, but make sure the number of lines printed is         equal to the original lines in the poem (Line numbers do not need to be printed.)
      
   4. **lines_printed_custom()**:
      -  It should minimally have 1 parameter called *lines_list*, which is a list of strings containing lines of your poem.
      -  It should print the poem in a unique way, be creative!
      
      ***For this, I used the sorted(lines_list, reverse=True) function to print the list in*** reverse alphabetical ***order***
