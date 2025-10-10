# create class
from tokenize import String


class IOString():


      # constructor to set default value
    def __init__(self):
        self.str1 = ""

        #function to get input from user
    def get_string(self):
        self.str1 = input("Enter String : ")

        # function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())

 # Object creation
ob = IOString()

    # Call functions
ob.get_string()
ob.print_String()