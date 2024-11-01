# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

#1: Item Counter

#Assume a file containing a series of names (as strings) is named names.txt and exists on the computer's disk.  

#Write a program that displays the number of names that are stored in the file.


#open names.txt file in read mode
namefile = open("names.txt", "r")
name = namefile.readline()

#loop through all records in file
#while record is not equal to blank string
while name != ' ':
	#set count at 0
	count = 0
	#see what name the program is on
	print(namefile.readline())
	#see what number the program is on
	print(f"{name} is number {count}")
	#add to count
	total_count = count + 1

#continue to read
name = author_readline()
#in read mode
name = name.rstrip('')

if name == '':
	print(f"total: {total_count}")

#close	
namefile.close()