# Errors happen in programs, and we need a way to handle them. 
# Causes error since can't divide by zero, try then create exception.
try:
    x = 10/0
except:
    print("Cannot divide by zero.")

# You can also catch specific exceptions
try:
    answer = input("What should I divide by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e: 
    print("You can't divide by zero!")
except ValueError as e: 
    print("You didn't give me a valid number!")
    print(e)
# Finally executes a code block regardless of caught exception.
finally:
    print("This code always runs.")
    
