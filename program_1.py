#1: Item Counter

#Assume a file containing a series of names (as strings) is named names.txt and exists on the computer's disk.  

#Write a program that displays the number of names that are stored in the file.


#open names.txt file in read mode
namefile = open("names.txt", "r")
name = "name"

#set count at 0
count = 0

#loop through all records in file
#while record is not equal to blank string
while name != '':
	#see what name the program is on
	name = namefile.readline()
	#see what number the program is on
	print(f"{name} is number {count}")
	#add to count
	count += 1

#accounting for adding one extra count in while loop
count -= 1

#display total
if name == '':
	print(f"total: {count}")

#close	
namefile.close()