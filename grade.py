e = float(input("english="))
pe = float(input("hindi="))
phy = float(input("physics="))
c = float(input("chemistry="))
b = float(input("biology="))

print("Total Marks =",(e+pe+phy+c+b))

p=((e+pe+phy+c+b)/500)*100

print(p,"%") 

if(p>90):
	grade= "A+"
elif(p>80):
	grade= "A"
elif(p>70):
	grade= "B+"
elif(p>60):
	grade="B"
elif(P>50):
	grade="C+"
elif(p>40):
	grade="C"
elif(P>34):
	grade="D"
else:
	print("fail")
	grade="F"

print(grade)

