# Get user input for start and end values
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


# Genearte sqaure valures in the specified range
squares = [i**2 for i in range(start, end + 1)]

# Seperate into even and odd square values
even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

# Output the results
print("\nAll square values:", squares)
print("Even sqaure values:", even_squares)
print("Odd sqaure values:", odd_squares)