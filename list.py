print(" \n\n program for execution of functions of list and sequences\n\n")




lst1=[1,2,6,69,88]
sum=0
for x in range(0,len(lst1)):
	print(lst1[x])
	sum=sum+lst1[x]
lst1[2]=20
print(lst1)
print("\n",sum,"\n")
print("\n\n-------------------------------------------------------------------------------------\n\n")
print(" \n\n use of append function\n\n")


n=int(input("\n\nenter the size of list\n\n"))

lst=[]
sum=0
for x in range(0,n):
	lst.append(int(input("enter the element ")))
	sum=sum+lst[x]

print("avg ",sum/n)
print("\n",lst)


print("\n",max(lst))

lst.sort()

print(lst)

print("\n minimum element in the list is ",min(lst))

#print("\n sum= ",sum(lst))

#print("\n avg= ",avg(lst))

print("\n length= ",len(lst))

lst.extend(lst1)

print(lst)

#check for sort , avg, sum, extend function not working
print("\n\n-------------------------------------------------------------------------------------\n\n")
print(" \n\n function over string\n\n")

ls=[]
sum=" "
for x in range (0,3):
	ls.append(input("enter the string "))

ls1=["k","o","u"]

print(ls)

print(ls.extend(ls1))

print(ls.reverse)





