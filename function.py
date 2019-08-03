def smaller(x,y,z):
	if (x<y and x<z):
		print("x is smaller among all and the value is ", end=" ")
		return x
	if (y<z and y<x):
		print("y is smaller among all and the value is",end=" ")
		return y
	if (z<x and z<y):
		print("z is smaller among all and value is",end=" ")
		return z

x=int(input("enter the value of x\t"))
y=int(input("enter the value of y\t"))
z=int(input("enter the value of z\t"))

print(smaller(x,y,z))