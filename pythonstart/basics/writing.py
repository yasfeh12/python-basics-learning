# Reading
file_path = 'scraped_quotes.csv'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Iterate over each line in the file and print it
    for line in file:
        print(line.strip())  # Use .strip() to remove any trailing newline characters

# write
data = [
    "This is the first line.",
    "This is the second line.",
    "And this is the third line."
]

# Open the file in write mode
with open(file_path, 'w') as file:
    # Iterate over each line of data
    for line in data:
        # Write each line followed by a newline character
        file.write(line + '\n')
