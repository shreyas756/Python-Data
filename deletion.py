lst=[]

for x in range(0,4):
	lst.append(input("string char\t"))
lst.pop(1)
n=input("enter the element to be deleated")
lst.remove(n)
print("\n",lst,"\n")