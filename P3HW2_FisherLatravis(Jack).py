#CTI-110
#P3HW2-Salary
#Fisher Latravis (Jack)
#11/21/2023
#Use if/else to determine an employees pay

emp_name = input("Enter Employee Name:")
emp_hours = int(input("Enter Employee's hours: "))
emp_pay = float(input("Enter the Employee's pay rate: "))

#Calculations
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hours = 40

#This represents if emp_hours is 40 or less
else:
    ot_hours = 0
    reg_hours = emp_hours

#Calculate Pay
ot_pay = (emp_pay * 1.5) * ot_hours
reg_pay = emp_pay * reg_hours
gross_pay = ot_pay + reg_pay

print(f"Employee Name: {emp_name}")
print(f"Regular Hours: {reg_hours}")
print(f"OT Hours: {ot_hours}")
print(f"Regular Pay: {reg_pay}")
print(f"Gross Pa: {gross_pay}")
