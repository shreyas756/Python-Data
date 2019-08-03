def percen(lst):
	sum=0.0
	per=0.0
	for x in lst:
		sum+=float(x)
	per=sum/len(lst)
	return per

def sort(lst):
	n=len(lst)
	for i in range(n-1,-1,-1):
		for j in range(0,i):
			if (lst[j][2]>lst[j+1][2]):
				lst[j],lst[j+1]=lst[j+1],lst[j]

file=open('file.csv','r') 
result=open('result.txt','w')
above60=[]
bet5060=[]
below50=[]

for line in file:
	line=line.strip()
	lst=line.split(",")
	print(lst)
	per=percen(lst[2:])
	
	if (per>60):
		above60.append([lst[0],lst[1],per])	
	elif (per<60 and per>50):
		bet5060.append([lst[0],lst[1],per])
	else:		
		below50.append([lst[0],lst[1],per])
sort(above60)
sort(bet5060)
sort(below50)

result.write("The student got more than 60% are:-{}\n".format(len(above60)))
for x in above60:
	result.write(str(x)+"\n")

result.write("The student got bet 50-60 are:-{}\n".format(len(bet5060)))
for x in bet5060:
	result.write(str(x)+"\n")

result.write("The student less than 50 are:-{}\n".format(len(below50)))
for x in below50:
	result.write(str(x)+"\n")

result.close()




