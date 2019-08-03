def cube(a):
	return a**3
def square(a):
	return a**2
def listmap(lst,fun):
	nlst=[]
	for x in lst:
		nlst.append(fun(x))
	return (nlst)

lst=[]
n=int(input())
for x in range(n):
	lst.append(int(input("enter the list element")))
print(listmap(lst,cube))
print(listmap(lst,square))
