def fab(z):
	fab=0
	p,q=0,1
	print(p,q,end=" ")
	for x in range (0,(z-2)):
		
		fab=p+q
		p,q=q,fab
		print(fab,end=" ")
z=int(input("enter the length of series"))
fab(z)