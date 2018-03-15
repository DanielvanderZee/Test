''' Program make a simple calculator that can add, subtract, multiply and divide'''

# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Bladibla.")
print("Select operation. ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = int(input("Enter choice(1/2/3/4):"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
   print(str(num1)+ "+" +str(num2) + "=" + str(add(num1,num2)))

elif choice == 2:
   print(str(num1) + "-"+ str(num2) + "=" + str(subtract(num1,num2)))

elif choice == 3:
   print(str(num1) + "*" + str(num2) + "=" + str(multiply(num1,num2)))

elif choice == 4:
   print(str(num1) + "/" + str(num2) + "=" + str(divide(num1,num2)))
else:
   print("Invalid input")
