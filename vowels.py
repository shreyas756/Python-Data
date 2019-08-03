str=input("enter the string ").lower()
v="aeiou"
count=0
for i in range (0,len(str)):
	
	if (str[i] in v):
		count=count+1
#if (count>0):
#	print(" vowels are present in string")	

	
print(count, "vowels present")
