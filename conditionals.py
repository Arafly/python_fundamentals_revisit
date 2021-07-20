# Single conditional
# price = input("How much did you pay? ")
# price = float(price)

# if price >= 1.00:
#     tax = .07
# else:
#     tax = 0
# print(tax)

# Multiple conditions
# Various Candian provinces and their tax rates
# country = input("Enter your Country here: ")

# if country.lower() == 'canada':
#     province = input("Enter your province here: ")
#     if province in ('Alberta',\
#         'Waterloo', 'Nunavut', 'Yukon'):
#         tax = 0.05
#         print(tax)
#     elif province == 'Ontario':
#         tax = 0.13
#         print(tax)
#     else:
#         tax = 0.15
#         print(tax)
# else:
#     tax = 0.0
#     print(tax)
    

# Calculating scores to be in the Honour's list
# A student makes the Honour Roll if their average is >=85
# and their lowest grde is NOT below 70
gpa = float(input("Enter your GPA here please: "))
lowest_grade = float(input("And now your lowest grade: "))

if gpa >= .85 and lowest_grade >= .70 :
    print("\nWell done, you're made the list!")
    honour_roll = True
else:
    print("\nSorry you didn't make it")
    honour_roll = False
    
