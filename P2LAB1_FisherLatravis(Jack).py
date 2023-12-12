#Fisher Latravis (Jack)
#11/14/2023
#Use float value to represent the cost to drive a specifided distance

#Get input from user
mpg = float(input("Enter the car's mpg as a decimal number: "))
cost_gal = float(input("Enter the cost for gallon of gas: "))

#Calculate cost to drive 20 miles
drive_cost_20 = (20/mpg) * cost_gal

#Calculate cost to drive 20 miles
drive_cost_75 = (75/mpg) * cost_gal

#Calculate cost to drive 20 miles
drive_cost_500 = (500/mpg) * cost_gal

#Output the costs with 2 decimal places using an f-string
print (f"Cost to drive to 20 miles is {drive_cost_20:.2f}")

#Output the costs with 2 decimal places using an f-string
print (f"Cost to drive to 75 miles is {drive_cost_75:.2f}")

#Output the costs with 2 decimal places using an f-string
print (f"Cost to drive to 500 miles is {drive_cost_500:.2f}")
