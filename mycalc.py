#Defining functions for adding, subtracting, multiplying, and dividing numbers
def add(one, two):
    return one + two

def subtract(one, two):
    return one - two

def multiply(one, two):
    return one * two

def divide(one, two):
    return one / two

#introduction
print("Welcome to the simple calculator! Please follow the instructions on your screen to proceed")

#Prompt for first integer
one=(int(input("Enter First Integer: ")))
while one==0:
    print("Error: Please Enter a Nonzero Integer")
    one=(int(input("Enter First Integer: ")))

#Displaying list of operation options
print("Please choose an operation: \n" \
      "1. Add \n" \
      "2. Subtract \n" \
      "3. Multiply \n" \
      "4. Divide \n")

#Receiving input from user
operation=(int(input("Select Operation from numbered list: 1-4: ")))
while operation > 4 or operation < 1:
    print("Error: Please select a number 1-4")
    operation=(int(input("Select Operation from numbered list: 1-4: ")))

#Prompt for second integer
two=(int(input("Enter Second Integer: ")))
while two==0:
    print("Error: Please Enter a Nonzero Integer")
    two=(int(input("Enter Second Integer: ")))

#solving equation and printing result
if operation==1: print(one, "+", two, "=", add(one,two))
elif operation==2: print(one, "-", two, "=", subtract(one, two))
elif operation==3: print(one, "*", two, "=", multiply(one, two))
elif operation==4: print(one, "/", two, "=", divide(one, two))

print("Please rerun program if more calculations are needed. Goodbye")



                
