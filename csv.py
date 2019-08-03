file=open('csvfile.csv','r')

def max(mark):
	max=mark[0]
	i=[]
	for x in range(1,len(mark)):
		if(max < mark[x]):
			max=mark[x]
		
	i.append(max)
		
	print(i)
	


roll=[]
name=[]
mark=[]

for line in file:
	line=line.strip()
	lst=line.split(",")
	roll.append(lst[0])
	name.append(lst[1])
	mark.append(lst[2])

max(mark)

