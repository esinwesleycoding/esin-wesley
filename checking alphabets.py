def is_alphabet(char):
    if len(char) != 1:
        print("Please enter a single character.")
    elif char.isalpha():
        print(f" '{char}' is an alphabet.")
    else:
        print(f" '{char}' is NOT an alphabet.")

# Example usage
user_input = input("Enter a character: ")
is_alphabet(user_input)
