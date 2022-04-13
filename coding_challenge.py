# Automate copying files from folder1 to folder2 every 30 seconds

# provide access to operating system functionality
import os

# For accessing date and time
from datetime import datetime, time

# For copying files, provide high-level operations on files and collections of files
import shutil

# provides various time-related functions
import time

# Get the current time for displaying
program_start_time = datetime.now()

# Display the current time
print("Program started at :-" + " " +str(program_start_time.strftime("%H:%M:%S,%m/%d/%Y")))

# watch folder that need to be assesed for changes in file number
watch_folder = "folder1"

# get list of all files only in the given directory before the loop started
before = list(f for f in os.listdir (watch_folder))

# variable for storing count of files copied
count = 0

# loop for running the program infinitely
while True:

	# pause for 30 seconds
  	time.sleep (30)

  	# loop start time for displaying scanning time
  	start_time = datetime.now()

  	# get list of all files only in the given directory after 30 seconds
  	after = list(f for f in os.listdir (watch_folder))

  	# Display the scanning time
  	print("-------------------------------------------------------------------")
  	print("Scanned at :-" + " " + str(start_time.strftime("%H:%M:%S,%m/%d/%Y")))

  	# acquire all files names added to the folder
  	added = list(f for f in after if not f in before)

  	# create a empty list to store files names that are coied
  	file_copied = list()

  	# loop over the list of new files
  	for files in added:

  		# Add the file names that are copied to be displayed
  		file_copied.append(files)

  		# Create the file path for copying to folder2
  		file_path = os.path.join(watch_folder,files)

  		# Copy the files to folder2 
  		shutil.copy(file_path, "folder2")

  		# Count the total number of files copied 
  		count = count + 1

  	# assign after dir list to before dir list
  	before = after

  	# Print total files copied
  	print("Total file copied :-" + " " + str(count))

  	# statement for printing scanning info and files copied
  	if len(file_copied) == 0:
  		print("Files copied during the current scan :-" + " " + "None")
  		print("-------------------------------------------------------------------")
  	else:
  		print("Files copied during the current scan :-" + " " + str(file_copied)[1:-1])
  		print("-------------------------------------------------------------------")