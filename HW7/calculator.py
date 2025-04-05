import math_tools as mt

a=float(0)
b=float(0)
opp='error'
g=1
g=1
c=""
a=float(input("Enter the first number to be used in the operation: "))
b=float(input("Enter the second number to be used in the operation: "))
opp=input("Enter operation(ENTER either 'add','substract','multiply', or 'divide': ")
if (opp=="add" or opp=="ADD" or opp=="Add"):
		c=mt.add(a,b)
elif (opp=="Substract" or opp=="SUBSTRACT" or opp=="substract"):
		c=mt.substract(a,b)
elif (opp=="multiply" or opp=="Multiply" or opp=="MULTIPLY"):
		c=mt.multiply(a,b)
elif (opp=="divide" or opp=="Divide" or opp=="DIVIDE"):
		c=mt.divide(a,b)
else:
	print('something went wrong as' + opp + 'is not a supported function. Please try again.')
	g=0
if g!=0:
	print("result:", + c)