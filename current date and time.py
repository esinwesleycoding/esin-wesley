from datetime import date , time , datetime


# calling the toda
# function of date class
today = date.today()
now = datetime.now()
print("Today's date is", today)



# Printing date's components
print("\nDate components", today.year, today.month, today.day)