print("\t program to find and eliminate the word from string and convert the remaining string to list\t\t ")

str=input("enter the string \n\n")
lst=[]
lst=str.split()
newlst=[]
n=input("enter the element to be eliminated")

for x in (lst):
	if (n.lower()!=x.lower()):
		newlst.append(x)

print(" ".join(newlst))