base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))


result = 1
for i in range(exponent):
    result = result * base

print(base, "raised to power", exponent, "is", result)