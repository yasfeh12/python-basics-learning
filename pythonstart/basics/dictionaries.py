##simular to obj
month_conversions = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

print(month_conversions["nov"])
print(month_conversions.get("dek", "a not valid key "))
# .get() allows us top set a defult value which is returned instead of none if the key given is invalid. 
#we can use numbers/ indexs in a dictionary