from sympy import isprime
import numpy as np

ar1 = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
def avpr(ar1):
	hi=int(ar1.shape[0])
	wi=int(ar1.shape[1])
	tar=[]
	pr=0
	ax=0
	for i in range(hi): #move down
		for j in range(wi): #prime attach
			k=0
			
			while (k<wi) and (pr==0): #Prime check
				if (isprime(int(ar1[i,j]))):
					pr=1
				else:
					pr=0
				k+=1
		if pr==1:
			pr=0
			tar.append(list(ar1[i]))
			ax+=1
	return np.array(tar)
arp1=avpr(ar1)
print(arp1)
#2.1
print("2.1")

def chkr():
  return np.zeros((8,8))
brd=chkr()
print(brd)
#2.2
print("2.2")
def chkr():
  brd=np.zeros((8,8))
  a=1 #WHY ARE THESE ALL SO DIFFICULT UNNECESSARILY?? AM I DOING THIS WRONG? THIS FEELS LIKE AN EXCERCISE IN LOGIC AND I AM NOT QUITE KEEPING UP.
  for i in range(8):
    for j in range(8):
      if (a==1) and i%2!=1:
        brd[i,j]=1
        a=2
      elif (a==2) and i%2!=1:
        brd[i,j]=0
        a=1
      elif (a==1) and i%2==1:
        brd[i,j]=0
        a=2
      elif (a==2) and i%2==1:
        brd[i,j]=1
        a=1
  return np.array(brd)
brd=chkr()
print(brd)

#2.3
print("2.3")
def chkrr():
  brd=np.zeros((8,8))
  a=1 
  for i in range(8):
    for j in range(8):
      if (a==1) and i%2!=1:
        brd[i,j]=0
        a=2
      elif (a==2) and i%2!=1:
        brd[i,j]=1
        a=1
      elif (a==1) and i%2==1:
        brd[i,j]=1
        a=2
      elif (a==2) and i%2==1:
        brd[i,j]=0
        a=1
  return np.array(brd)
brdr=chkrr()
print(brdr)
#3
print("3")
universe=np.array(['galaxy','clusters'])
def ep(var,sp):
  exp=[]
  expf=[]
  for i in range(len(universe)):
    expt=[]
    exps=""
    for j in range(len(universe[i])):
      count=sp
      expt.append(universe[i][j])
      exps=exps+universe[i][j]
      while count>0:
        exps=exps+" "
        count-=1
      
    exp.append(str(exps))
  return (exp)

sp=2
exp=ep(universe,sp)
print(exp)
#4
print("4")
#I spend an entire hour on this before deciding to loop for other ways. I have no idea if any functions were listed.
def stars(arr):
  print("array:\n", arr)
  arrt=np.transpose(arr)
  print(arrt)
  arsrt=np.vsort(arrt)
  print(arset)
  return np.transpose(arsrt)[1]
array1 = np.random.randint(500, 2000, (5, 5))
a=stars(array1)
print("2nd smallest:\n",a)
