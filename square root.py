import math

def calculate_square_root():
    try:
        number = float(input("Enter a number to find its square root: "))
        
        if number < 0:
            print("Error: Cannot calculate the square root of a negative number.")
        else:
            sqrt_value = math.sqrt(number)
            print(f" The square root of {number} is {sqrt_value:.4f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the function
calculate_square_root()
