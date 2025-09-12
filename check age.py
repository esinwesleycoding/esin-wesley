def check_age_range():
    try:
        age = int(input("Enter your age: "))
        
        if 10 <= age <= 20:
            print("You are between 10 and 20 years old.")
        else:
            print("You are NOT between 10 and 20 years old.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the function
check_age_range()
