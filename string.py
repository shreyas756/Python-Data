str=input("enter String  ")
print("\n")
print(str)
print("\n")
print(str.upper())
print(str[3]+"\n")
print(len(str))
print("\n")												  
print(str)
print("\n")
print(str[0:len(str)])
print("\n")
ss=input(" enter the substring  ")

if(ss in str):
	print(ss+" is sub string of "+str)
else:
	print("not a substring")

print(str.find(ss))
print("\n")
print(str.find(ss,3,9))


#check if \n can be concanated with function and methods
#find function is returning 0 value