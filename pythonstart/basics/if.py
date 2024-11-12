is_male=False
is_tall=True
if is_male or is_tall:
    print("cutie")
elif is_male and is_tall:
     print("hey handsome")
elif not(is_male) and is_tall:
     print("long leg lady")
else: 
    print("short and weak?")
 
def maxnum(num1,num2,num3):
     if num1>=num2 and num1>=num3:
          return num1
     elif num2>=num1 and num2>=num3:
          return num2
     else:
          return num3
    
print(maxnum(1,40,8))
## == is equal
#!= nopt ewual to. 
