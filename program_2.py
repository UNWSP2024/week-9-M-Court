# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

#import random
import random
#create integer list
random_number_list = []

def find_user_range():
	#get a number from user.
	user_range = int(input("enter a number (between 1-1000): "))

#set paramaters for user range
	try:
			if user_range >= 1 and user_range <= 100:
					#add total
					return user_range
	except:
			if user_range < 1 or user_range > 100:
					print("Number out of range.")

def make_list(user_range):
			for numbers in range(user_range):
					#create random list with user range
					random_number_list = math.random()
			return random_number_list

def list_into_string(random_number_list):
			#make the integer list into a sring 
			string_list = str(random_number_list)
				
			#close file
			open_number_file.close()
				
			#return new string
			return string_list

#get user range with function
find_user_range()
#make list with the range user entered
make_list(range)
#make list into string 
list_into_string(random_number_list)
#write string list to file
open_number_file.write(string_list)

