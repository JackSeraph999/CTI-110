#Travel Budget
#11/16/2023
#CTI-110 P1HW2-TRAVEL EXPENSES
#Fisher Latravis (Jack)
#

budget = int(input("Enter your budget"))
travel = input("Enter your travel destanation")
gas = int(input("Enter cost of gas"))
accomodation = int(input("Enter cost for accomodations"))
food = int(input("Enter cost of food"))

total = budget - (gas + accomodation + food)

print('New total is:', total)


