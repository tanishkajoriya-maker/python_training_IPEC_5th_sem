""" Program to Calculate Compound Interest with Validation"""

p = float(input("Enter the Principal Amount: "))
r = float(input("Enter the Rate of Interest (%): "))
t = float(input("Enter the Time (in years): "))

if p > 0 and r >= 0 and t > 0:
    amount = p * (1 + r / 100) ** t
    ci = amount - p

    print("Compound Interest =", round(ci, 2))
    print("Total Amount =", round(amount, 2))
else:
    print("Invalid Input! Principal and Time must be greater than 0, and Rate cannot be negative.")
    """output: Enter the Principal Amount: 200
Enter the Rate of Interest (%): 55
Enter the Time (in years): 2
Compound Interest = 280.5
Total Amount = 480.5"""

=== Code Execution Successful ===