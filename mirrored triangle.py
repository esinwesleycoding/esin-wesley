def mirrored_right_triangle(height):
    """
    Prints a mirrored right triangle of given height.

    Parameters:
    height (int): The number of rows in the triangle
    """
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * i
        print(spaces + stars)

# Example usage
try:
    h = int(input("Enter the height of the triangle: "))
    if h <= 0:
        print("Height must be a positive integer.")
    else:
        mirrored_right_triangle(h)
except ValueError:
    print("Please enter a valid integer.")
