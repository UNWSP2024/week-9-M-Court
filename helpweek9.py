#this program displays the contents of a file

def main():
	#get the name of a file.
	userfilename = input("Enter a filename: ")
	
	try:
		#open the file.
		insidefile = open(userfilename, "r")
	
		#read the contnts
		contents_of_file = insidefile.read()
			
		#display the file's contents
		print(contents_of_file)
			
		#close the file
		insidefile.close()
			
	except IOError:
		print('An error occured trying to read')
		print('the file', userfilename)

#call the main function
if __name__ == '__main__':
	main()
