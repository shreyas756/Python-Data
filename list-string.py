print("\n\n program for conversion string to List and via verse \n\n")

#print("\n\nlist to string conversion\n\n")
lst=[]

for x in range (0,4):
	lst.append(input("enter the list of element "))
	print(lst)

str=" ".join(lst)

print("\n"+str+"\n")


print("\n\n-------------------------------------------------------------------------------------\n\n")

st=input("enter the string  ")

print(list(st))

print(st.split())

				

