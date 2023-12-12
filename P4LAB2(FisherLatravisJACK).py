#Fisher Latravis(Jack)
#11/28/2023
#Using a For Loop with range function
#

#Get input from the user

num1 = int(input("Enter an interger: "))
num2 = int(input("Enter an higher than the first interger: "))

#If the first number is smaller
if num1 < num2:
    for i in range(num1, num2 + 1, 5):
     print(i)
else:
    #While the input is invalid
    while num1 > num2 or num1 == num2:
        print("First number must be smaller")

        #Get input from the user
        num1 = int(input("Enter an interger: "))
        num2 = int(input("Enter an higher than the first interger: "))
    for i in range(num1, num2 + 1, 5):
        print(i)
