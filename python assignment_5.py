#!/usr/bin/env python
# coding: utf-8
1. Write a Python Program to Find LCM?
# In[ ]:


# Python program to find the L.C.M. of two input number

# This function computes GCD (Greatest Common Divisor)
def compute_gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

#This function computes LCM

def compute_lcm(x,y):
    lcm=(x*y)//compute_gcd(x,y)
    return lcm
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("The L.C.M. is", compute_lcm(num1, num2))

2. Write a Python Program to Find HCF?
# In[ ]:


# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):
    

# choose the smaller number
    if x > y:
        
        smaller = y
    else:
        
        smaller = x
    for i in range(1, smaller+1):
        
        if((x % i == 0) and (y % i == 0)):
            
            hcf = i 
    return hcf

num1 =int(input("Enter the first number:"))
num2 =int(input("Enter the second number:"))

print("The H.C.F. is", compute_hcf(num1, num2))

3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# In[ ]:


#predefined functions code to convert decimal to binary,octal and hexadecimal
decimal = int(input("Please Enter the Decimal Number = "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(decimal, " Decimal = ", binary, "Binary Value")
print(decimal, " Decimal = ", octal, "Octal Value")
print(decimal, " Decimal = ", hexadecimal, "Hexadecimal Value")


# In[ ]:


#program to convert decimal to binary
def DecimalToBinary(number):
     

    if number >= 1:

        DecimalToBinary(number // 2)

    print(number % 2, end = '')


# Driver Code

if __name__ == '__main__':


    # decimal value

    decimal_val = int(input("enter the number:"))


    # Calling function

    DecimalToBinary(decimal_val)


# In[ ]:


#Program to convert decimal to octal
def decToOctal(num):

    # array to store

    # octal number

    octalNumber = [0] * 100

 

    # counter for octal

    # number array

    i = 0

    while (num!= 0):

        # storing remainder

        # in octal array

        octalNumber[i] = num % 8

        num = int(num / 8)

        i += 1

    # printing octal number

    # array in reverse order

    for k in range(i - 1, -1, -1):

        print(octalNumber[k], end="")

# Driver Code

num =int(input("Enter the number:"))

# Function Call

decToOctal(num)


# In[ ]:


#program to convert decimal to hexadecimal
def decToHexa(num):
    # char array to store
    # hexadecimal number

    hexaDeciNumber = ['0'] * 100
    # counter for hexadecimal
    # number array

    i= 0

    while(num!= 0):
        # temporary variable

        # to store remainder

        temp = 0

        # storing remainder
        # in temp variable.

        temp = num % 16

        # check if temp < 10

        if(temp < 10):

            hexaDeciNumber[i] = chr(temp + 48)

            i = i + 1

        else:

            hexaDeciNumber[i] = chr(temp + 55)

            i = i + 1

        num = int(num / 16)

     # printing hexadecimal number

    # array in reverse order

    j = i - 1

    while(j >= 0):

        print((hexaDeciNumber[j]), end="")

        j = j - 1

# Driver Code

num =int(input("Enter the number:"))

decToHexa(num)

4. Write a Python Program To Find ASCII value of a character?
# In[ ]:


# Program to find the ASCII value of the given character

c = input("Enter the character:")
print("The ASCII value of '" + c + "' is", ord(c))
    

5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# In[1]:


# Program make a simple calculator

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


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
          
    
    else:
        print("Invalid Input")


# In[ ]:




