def capital(x):
	return x.upper()
def listmap(lst,fun):
	nlst=[]
	for x in lst:
		nlst.append(fun(x))
	
	return nlst
lst=['ajay','vijay','sanjay']
print(lst,"\n")
print(listmap(lst,capital))

	