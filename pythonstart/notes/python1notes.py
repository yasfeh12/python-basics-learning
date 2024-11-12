# Some Keypoints I noted down:

# Python:

# Always typecast your input
# Default input is always string

# *List:
#  - List can store multiple data types at a time (can be changed)
#  - List Functions:
#    f1.extend(f2) - adds two lists
#    f1.insert(index, f1) - inserts an element
#    f1.remove(value) - removes the element
#    f1.pop() - removes last element from the list
#    f1.count(value) - counts occurrences of a value
#    f1.reverse() - reverses the order of the list
#    f2 = f1.copy() - creates a copy of a list

# *Tuple:
#  - Similar to a list, but cannot be changed once declared
#  - Use normal parentheses, not square brackets
#  - Example: ex_tuple = (4, 5)

# *Function:
#  - Keyword: def
#  - Example: def ex_func():
#  - Every function needs to be called to be executed

# *IF:
#  - Logical operators: or (||), and (&&), not() - negates condition
#  - Syntax:
#      if condition1:
#      elif condition2:
#      else:

# *Dictionaries:
#  - Allows accessing values by keys
#  - Example:
#      ex_dic = {
#          "Jan": "January",
#          "Feb": "February"
#      }
#  - Using get() method to avoid invalid key errors:
#      print(ex_dic.get("Jan", "Invalid"))

# *While:
#  - Syntax:
#      while condition:
#          # Code block

# *For:
#  - Syntax:
#      for variable in range(range_limit):
#          # Code block

# *2D List:
#  - Example:
#      ex_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
#  - Nested loops to print each element:
#      for row in ex_2D:
#          for col in row:
#              print(col)
#  - Output:
#      All elements printed one by one

# *Comments:
#  - Use # to start a comment

# *Try/Except:
#  - Handles user input errors
#  - Syntax:
#      try:
#          # Code that might cause an error
#      except TypeOfError:
#          # Code to execute if an error occurs

# *Read files:
#  - If you open a file, always close it after
#  - Example:
#      file = open("file.txt", "r")  # Opens file in read mode
#      print(file.readable())  # Returns a boolean for readability
#      file.close()
#  - readlines() - converts each line to an element in a list

# *Write files:
#  - file = open("file.txt", "a")  # Appends to a file
#  - file = open("file.txt", "w")  # Overwrites a file
