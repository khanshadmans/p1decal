#HW3 SP2025
#1)
def computePower(x,y):
	pw=1
	if y!=0:
		for i in range(y):
			pw*=x
	print("1:\n>",pw)
	return pw
x = 2
y = 3
computePower(x, y)
#2
def tempRan(read):
	high=max(read)
	low=min(read)
	print ("2:\n>","(",low,',',high,')')
"""    low=read[1]
	high=read[1]
	for i in read:
		if low>i:
			low=i
		if high<i:
			high=i
			"""
read = [15, 14, 17, 20, 23, 28, 20]
tempRan(read)      
(14, 28)
#3
def Wknd(day):
	yes="False"
	if day==6 or day==7:
		yes="True"
	print("3:\n>",yes)
day = 6 # Saturday
Wknd(day)
True
#4
def feff(dis,oil):
	print("4:\n>",round(dis/oil, 2))
dis = 70 # miles
oil= 21.5 # gallons
feff(dis,oil)
3.26
#5
def dcdNum(n):
	a=n//10
	b=n%10
	print("5:\n>",b*10000+a)
n = 12345
dcdNum(n)
51234
#6.1
def fmin(n):
	low=n[0]
	for i in read:
		if low>i:
			low=i	
	print("6.1:\nlow:\n>",low)
def fmax(n):
	high=n[0]
	for i in read:
		if high<i:
			high=i	
	print("high:\n>",high)
n = [2024, 98, 131, 2, 3, 72]
fmin(n)
2
fmax(n)
2024
#6.2
def wmin(n):
	low=n[0]
	lm=len(n)
	i=0
	while i<lm:
		if low>n[i]:
			low=n[i]
		i+=1
	print("6.2:\nlow:\n>",low)
def wmax(n):
	high=n[0]
	lm=len(n)
	i=0
	while i<lm:
		if high<n[i]:
			high=n[i]
		i+=1
	print("high:\n>",high)
n = [2024, 98, 131, 2, 3, 72]
wmin(n)
2
wmax(n)
2024
#7
def vowcons(txt):
	alp=0
	vow=0
	for i in range(len(txt)):
		if txt[i].isalpha()==True:
			alp+=1
			if txt[i]=="A" or txt[i]=="a" or txt[i]=="E" or txt[i]=="e" or  txt[i]=="I" or txt[i]=="i" or txt[i]=="O" or txt[i]=="o" or txt[i]=="U" or txt[i]=="u":
				vow+=1
	cons=alp-vow
	print("7:\n>(",vow,",",cons,")\nSomething went wrong because vowels is wrong in example!!!!")
txt = "UC Berkeley, founded in 1868!"
vowcons(txt)
(4, 11)
#8
def droot(num):
	h=str(num)
	l=len(h)
	tot=0
	for i in range(l):
		tot+=int(h[i])
	print("8:\n>",tot)
num = 2468
droot(num)
20
