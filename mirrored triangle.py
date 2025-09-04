def mirrored_right_triangle(height):
    
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * i
        print(spaces + stars)

# Example usage
h = int(input("Enter the height of the triangle: "))
if h <= 0:
    print("Height must be a positive integer.")
else:
     mirrored_right_triangle(h)

