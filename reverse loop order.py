# Ask the user to enter a number
user_input = input("Enter a number: ")

# Remove any negative sign or decimal point
clean_input = user_input.replace("-", "").replace(".", "")

# Count the digits
digit_count = len(clean_input)

# Display the result
print(f"Total number of digits: {digit_count}")
