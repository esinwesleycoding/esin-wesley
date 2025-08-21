n=int(input("enter the number:"))
number = 1
for i in range(n):
    for j in range(i+1):
        print(number ,end=" ")
        number = number + 1
    print()