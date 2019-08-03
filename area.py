b=input("enter the shape whose area is to be calculated ")

b=b.lower()

a=0
if (b == "square"):
	s=int(input("side of square"))
	a=s*s
elif (b == "rectangle"):
	l,b=int(input("length=")),int(input("breadth="))
	a=l*b
elif (b == "circle"):
	r=int(input("radius="))
	a=3.14*r*r
else:
	print("you entered unapprorite shape")

print(a)
