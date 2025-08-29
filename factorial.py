def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''


    if x==0 or x==1:
        return 1
    else:
        #calling function inside a fucntion
        return x*factorial(x-1)
    

#display result
print(factorial.__doc__)
print("the factoial of 0:",factorial(0))
print("the factoial of 1:",factorial(1))
print("the factoial of 4:",factorial(4))
print("the factoial of 5:",factorial(5))
print("the factoial of 10:",factorial(10))



