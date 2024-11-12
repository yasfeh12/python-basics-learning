# Defining a list of friends
friends = ["tom", "rhys", "luke", "josh", "mat", "frank", "michael"]
new_friends=["saul","g","huitton","maximus"]

# Accessing the first item in the list
print(friends[0])  # Output: "tom"

# Accessing the last item in the list using a negative index
print(friends[-1])  # Output: "michael"

# Slicing the list to get all items from the second item to the end
print(friends[1:])  # Output: ["rhys", "luke", "josh", "mat", "frank", "michael"]

# Slicing the list to get a specific range (from the second item up to, but not including, the fourth item)
print(friends[1:3])  # Output: ["rhys", "luke"]

friends.extend(new_friends)
new_friends.clear()

friends.append("the gays")
friends.pop()
friends.insert(1,"p diddy")
print(friends.index("p diddy"))
print(friends.count("p diddy"))
friends.sort()
friends.reverse()
final_friends=friends.copy()

print(friends)

##2d nested lists
number_grid=[[1,2,3],
             [4,5,6],
             [7,8,9],
             [0]]
##first []is up to down secpnd is left to right row then columb
print(number_grid[0][0])
print(number_grid[3][0])