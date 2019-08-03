import sys
if(len(sys.argv)<3):
	pass
else:
	src=open(sys.argv[1],"r")
	word=sys.argv[2:]
	for line in src:
		line=line.lower()
		for w in word:
			line=line.replace(w.lower(),w.upper())
		print(line,end=" ")