def reverse(lst,n):
	
	for x in range(0,n//2):
		
			lst[x],lst[len(lst)-1-x]=lst[len(lst)-1-x],lst[x]
#	print(lst)
	return lst

def sum(lst):
	sum=0
	for x in lst:
		sum+=x
#	print (sum)
	return sum

def avj(lst):
	avj=0
	sum=0
	for x in lst:
		sum+=x	
	avj=sum/(len(lst)-1)
#	print(avj)
	return avj
def max(lst):
	i=0
	max=lst[i]
	for x in range(0,(len(lst)-1)):
		if (max < lst[x+1]):
			max=lst[x+1]
			i=x+1	
#	print(max)
	return max	
			
def min(lst):
	min=lst[0]
	for x in range(0,(len(lst)-1)):
		if (min > lst[x+1]):
			min=lst[x+1]	
#	print(min)
	return min
	
if (__name__=="__main__"):
	lst=[]
	n=int(input("enter the size of list"))

	for x in range(n):
		lst.append(int(input()))
	print("\nreverse is",reverse(lst,n))
	print("\nsum is",sum(lst))
	print("\navj is",avj(lst))
	print("\nmax is",max(lst))
	print("\nmin is",min(lst))