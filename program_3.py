# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

#read open file
try:
		with open("numbers.txt", "r") as open_numbers_file:
				#read numbers
				number = int(open_numbers_file.readline())
				#make list
				number_total = []
				#add to total
				number_total + number
		
		#display total
		print(number_total)

#IOError 
except IOError:
		print("An error occured trying to read the file.")

#ValueError
except ValueError:
		print("non-numeric data found in the file.")

#other errors
#except:
	#	print("An error occured.")

