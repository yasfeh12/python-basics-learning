def power_by(base,power):
    result=1
    for index in range(power):
        result =result* base
    return result
print(power_by(5,5))