print("Enter a number less than 25")
number = int(input())  # Convert input from string to integer

if number > 25:
    print("Error")
else:
    while number <= 25:
        print("Inside the loop, my variable is", number)
        number += 1  # Increment the number to avoid infinite loop
