#while loop
i=1
while i<=10:
    print(i)
    i+=1
print("while loop done")
#for loops
friends=["tom","mat","rhys","luke"]
for letter in "yaseens world":
    print(letter)
print("for loop done")

for friend in friends:
    print(friend)
print("friend for loop done")

for index in range(3,7):
    print(index)
print("range for loop done")


##print all elments in array
for index in range(len(friends)):
    print(friends[index])
print("friends range for loop done")

for index in range(5):
    if index==0:
        print("first")
else:
    print("not first ")
print("friends range for loop done")

##nested loops
#print each array in nested array=>like resutructuring
number_grid=[[1,2,3],
             [4,5,6],
             [7,8,9],
             [0]]
for row in number_grid:
    print(row)
#print each item in nested array
for row in number_grid:
   for colum in row:
       print(colum)