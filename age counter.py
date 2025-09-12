def check_age():
    try:
        age = int(input("Enter your age: "))
        
        # Check if age is within a reasonable range
        if age < 0 or age > 130:
            print("Error: That doesn't seem like a valid age.")
        else:
            print("Age accepted.")
            if age % 2 == 0:
                print("Your age is even.")
            else:
                print("Your age is odd.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Run the function
check_age()
