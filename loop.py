
for r in range(1,6):
	for c in range(1,r+1):
		if((c%2)!=0):
			print("*",end="")
		else: 
			print(" | ",end="")
	print("")

print("\n using while loop\n")
#--------------------------------------------------------------------------------------------------------------


r=1
while(r<6):
	c=1	
	while(c<r+1):
		if((c%2)!=0):
			print("*",end="")
		else: 
			print(" | ",end="")
		c=c+1
	print("")
	r=r+1

print("\n\n change in pattern")
#--------------------------------------------------------------------------------------------------------------
# CHANGE IN PATTERN

for r in range(5,0,-1):
	for c in range(0,r):
		if((r%2)!=0):
			print(" * ",end="")
		else: 
			print(" | ",end="")
	print("")	

#-------------------------------------------------------------------------------------------------------------		
print("\n using while loop \n")


r=5
while(r>0):
	c=0
	while(c<r):
		if((r%2)!=0):
			print(" * ",end="")
		else: 	
			print(" | ",end="")
		c=c+1
	r=r-1
	print("")

print("\n\n-----------------------------------------------------------------------------\n\n")
	
for r in range(1,6):
	for c in range(1,6):
		if (r%5>1):
			if(c%5>1):
				print(" ",end="")
			else:
				print("*",end="")
		
		else:
			print("*",end=" ")
	print("")

        
print("\n\n-----------------------------------------------------------------------------\n\n")


for r in range(1,7):
	for c in range(1,7):
		if (r%6>1):
			if(c%6>1):
				print(" ",end=" ")
			else:
				print("*",end=" ")
		
		else:
			print("*",end=" ")

	print("")


print("\n\n-----------------------------------------------------------------------------\n\n")



for r in range(1,6):
	for c in range(1,6):
		if(c<r+1):
			print(c,end="")
	print("")


print("\n\n-----------------------------------------------------------------------------\n\n")
print("\n loop with addition\n")

for r in range(1,6):
	sum=0
	for c in range(1,r+1):
		print(c,end="")
		sum=sum+c		
	print(sum)	


print("\n\n-----------------------------------------------------------------------------\n\n")










		























