import sys
if (len(sys.argv)!=3):
	print("invalid arguments")
else:
	
	src=open(sys.argv[1],'r')
	dest=open(sys.argv[2],'w')
	print("enter the words you want to eliminate")
	n=int(input("no. of words you want to eliminate"))
	na=[]
	for x in range(0,5):
		na.append(input(x))	

	nlst=[]
	for line in src:
		lst=line.split()
	for y in na:
		for x in lst:		
			if (x.lower()==y.lower()):
				lst.remove(x)
	str=" ".join(lst)		
				
	
	dest.write(str)
	