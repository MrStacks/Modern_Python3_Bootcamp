from csv import reader
with open("fighters.csv") as file:
	csv_reader = reader(file, delimiter=",") #this only saves the "CSV reader object"
	for row in csv_reader:
		# each row is a list!
		print(row)
#iterating over the object (with the for loop) gives us a 
#nice iterator and each row in the CSV file is represented
#as a List
