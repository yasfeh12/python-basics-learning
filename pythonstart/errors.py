try:
    # value = 10 / 0  # Uncomment to test ZeroDivisionError
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as divide_by_zero_err:
    print("ZeroDivisionError:", divide_by_zero_err)

except ValueError as not_a_number:
    print("ValueError:", not_a_number)
