import sys
if (len(sys.argv)!=3):
	print("invalid argument")

else:
	#src=open(sys.argv[1],'r')
	#dest=open(sys.argv[2],'w')
	src=open(sys.argv[1],'rb+')
	dest=open(sys.argv[2],'wb+')
	print(src)
	dest.write(src.read())
	

	src.close()
	dest.close()