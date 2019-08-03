n=int(input("enter the total no. of element you want to sort "))
lst=[]
for x in range (0,n):
	lst.append(input("enter the element  "))
print ("unsorted list \t",lst)
p=(len(lst)-1)

while(p>0):
	q=0
	while(q<p):
		if(lst[q]>lst[q+1]):
			lst[q],lst[q+1]=lst[q+1],lst[q]
	
		q=q+1
	p=p-1

print ("\nsorted list \t",lst)  