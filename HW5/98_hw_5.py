'''
[Je m'appelle Judy. Bonjour.] or something.
i) You have been plopped into this directory system. What command will 
tell you what your working directory is?
	>pwd
ii) The command tells you ∼/python_decal/judy_decal. What command
with list all the files in your current working directory?
	>ls
iii) The command tells you ∼/python_decal/judy_decal. What command
with list all the files in your current working directory?
	> cd ../brianna_repo
iv) How would you move this new homework.py to your personal repository
homework directory?
	>cp homework.py ../judy_decal/homework
v) You want to see the contents of the homework.py in your terminal from
your personal repository. What command(s) will let you do this?
	>nano homework.py cat homework.py will only show what is in the inside??(Am I rememmbering this wrong?)
vi)	 You want to edit the contents of the homework.py in your terminal from
 your personal repository. What command will let you do this?
	>nano homework.py. cat probably can't edit??(Am I doing this wrong?)
vii) You have finished the homework. What commands will allow you to save
the changes and push from your local repository to your remote repository?
	>Git add . and then git commit.
viii)Oh no! Git gave you the following error. What commands should you call
 to resolve this error and push your homework properly? What does the
 error mean? (i.e. what did ”Judy” do wrong?)
	>She forgot to use git pull to get the updated file before making updates.
ix) What absolute path will allow you to move to Recents/?
	>cd ~/Recent
'''
#2
def dttyp(dt):
	return type(dt)
print("Q2")
dt="aleph"
print ("data:",dt)
typ=dttyp(dt)
print(typ)
dt=1.11111111
print ("data:",dt)
typ=dttyp(dt)
print(typ)
dt=1
print ("data:",dt)
typ=dttyp(dt)
print(typ)
dt=True
print ("data:",dt)
typ=dttyp(dt)
print(typ)
#3
def lssum(ls):
	sm=0
	for i in ls:
		sm+=int(i)
	return sm
ls=[1,2,3,4,5]
print('Q3:\n',ls, "\nsum:")
sm=lssum(ls)
print(sm)
#4.1
def lisdp(lis):
	nls=[]
	for i in lis:
		nls.append(i)
		nls.append(i)
	return nls
lis=[1,1,2,3,5,8,13,25]
print("Q4.1:", lis)
nls=lisdp(lis)
print(nls)
 #4.2
'''
def square(num)
	return num * num
 
The error is that the definition has no :
'''

print("Q4.2\ndef square(num):")
print("    return num * num")
print("Q5 enclosed")