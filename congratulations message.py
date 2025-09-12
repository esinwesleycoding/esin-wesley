def string_operations():
    name = input("Enter your full name: ").strip()

    print("\n String Analysis:")
    print(f"1. Original name: {name}")
    print(f"2. Uppercase: {name.upper()}")
    print(f"3. Lowercase: {name.lower()}")
    print(f"4. Title Case: {name.title()}")
    print(f"5. Number of characters (excluding spaces): {len(name.replace(' ', ''))}")
    print(f"6. First name: {name.split()[0]}")
    print(f"7. Reversed name: {name[::-1]}")
    print(f"8. Does your name contain 'a'? {'Yes' if 'a' in name.lower() else 'No'}")

# Run the function
string_operations()
