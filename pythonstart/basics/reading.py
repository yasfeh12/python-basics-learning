# Open the "scraped_quotes.csv" file in read mode and assign it to the variable "quotes"
with open("scraped_quotes.csv", "r") as quotes:
    # Read and print the entire contents of the file as a single string
    print(quotes.read())
    
    # Since .read() reads the entire file and moves the file pointer to the end,
    # calling .readline() or .readlines() afterward won't display anything
    # unless the file pointer is reset. Let's adjust the code to make use of each line correctly.

# Revised code with notes:

with open("scraped_quotes.csv", "r") as quotes:
    # Print the first line in the file using readline()
    print("First line:", quotes.readline().strip())  # Reads the first line only
    
    # Print the second line in the file using readline()
    print("Second line:", quotes.readline().strip())  # Reads the next line
    
    # Print all remaining lines as a list of lines using readlines()
    print("Remaining lines:", quotes.readlines())  # Reads all remaining lines
