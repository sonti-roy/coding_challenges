# An automated python script for copying files from folder1 to folder2 #

### Ensure that two folders with the names "folder1" and "folder2" are present in the current directory where the script is present.

### run the python script using the command 'python coding challenge.py' in the terminal

### All the library used comes preinstalled with python




# Pseudocode


> Save the watch folder into a variable


> Acquire a list of files present from before


> Set a variable to zero for storing the count of files copied later


> Create a while loop with 30 sec sleep time

>> 30-second sleep

>> Store the current time for displaying the scanning time

>> Get the list of all files only in the given directory at present

>> Get the files' names that are newly added by comparing them with the previous list

>> create an empty list to store files names that will be copied

>> run a for loop iterating over the newly added file list

>>> store the file names in the list for displaying later

>>> acquire the file path of the iterating files

>>> Copy the files using the file path to folder2

>>> count the number of files copied

>>> Assign the current list to the previous list

> Print all the messages














