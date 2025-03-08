#For the sake of keeping variables short, (L)i(s)t, 
#2.1: 
from typing import Concatenate


print("2.1")
ls1=list(range(21))
print(ls1)
'''
For the sake of 1.1, Error: "( was not closed" due to attempting a method.
I forgot to add the word Range in front, and doing so solved the issue.
'''
#2.2
print("2.2")
def two2(ls1):
	ls2=[]
	for i in ls1:
		tem=i**2
		ls2.append(tem)
	return ls2
ls2=two2(ls1)
print(ls2)
'''
1.1:
No significant errors
'''
#2.3
print("2.3")
def two3(ls2):
	return ls2[0:15]
ls3=two3(ls2)
print(ls3)
#2.4
print("Debug: ls2 =", ls2)
print("2.4")
def two4(ls2):
	return ls2[4::5]
ls4=two4(ls2)
print(ls4)
'''
Striding was causing an error by displaying the 6th value instead of the fifth.
Logic Error assumed.
Fixed by assigning the first value to be element 4 rather than 0. Further methods will be attempted and if this line exists, solution not found

'''
#2.5
print('2.5')
def two5(ls2):
	return ls2[::-3]
ls5=two5(ls2)
print(ls5)

'''
No significant errors
'''
#3.1
print("3.1")
def thr1():
	ma1=[]
	print(type(ma1))
	print(ma1)
	m=1
	for i in range(5):
		m1=[0,0,0,0,0]
		for j in range(5):
			m1[j]=m
			m+=1
		ma1.append(m1)
		
	return ma1
ma1=thr1()
print(ma1)


'''
Error:'NoneType' object has no attribute 'append' for the case ma1=ma.append(m1)
removed ma1 and left ma1.append(m1) and it is fixed.
'''

#3.2
print("3.2")
def thr2(ma1):
	for i in range(5):
		for j in range(5):
			if (ma1[j][i])%3 == 0:
				ma1[j][i]="?"
	return ma1
ma2=thr2(ma1)
print(ma2)
#3.3
print("3.3")
def thr2(ma2):
	summ2=0
	for i in range(5):
		for j in range(5):
			if (ma2[j][i])!="?":
				summ2+=ma2[j][i]
	return summ2
ma3=thr2(ma2)
print(ma3)