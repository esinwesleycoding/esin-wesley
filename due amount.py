# Input bill amount and payment
bill_amount = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid by the customer : "))

# Calculate due amount
if amount_paid < bill_amount:
    due = bill_amount - amount_paid
    print(f"Customer still has to pay: <{due:.2f}")
elif amount_paid > bill_amount:
    extra = amount_paid - bill_amount
    print(f"Customer overpaid by: <{extra:.2f}. Please return the balance.")
else:
    print("The bill is fully paid. No dues.")
