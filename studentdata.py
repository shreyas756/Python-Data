class Student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks=marks
        self.marks=list(map(int,marks))
        self.avg=sum(self.marks)/len(self.marks)
	
    def __del__(self):
        pass
	
    def get_roll(self):
        return self.roll
	
    def get_name(self):
        return self.name
    
    def get_marks(self):
        return self.marks

    def get_avg(self):
        return self.avg

    def get_data(self):
        return [self.roll,self.name,self.marks,self.avg]

    def __str__(self):
        return "Name--{}  AVG--{} ".format(self.get_name(),self.get_avg())
	

class StudentMap:
    def __init__(self,filename):
        self.file=open(filename,"r")
        self.write=open(f2,"w")
        self.stud_list=[]
        self.mapfile()
	
    def mapfile(self):
        for line in self.file:	
            line=line.strip()
            lst=line.split(",")
            self.stud_list.append(Student(lst[0],lst[1],lst[2:]))

    def student_list(self):
        return self.stud_list
    
    def write_list():
        pass       

    def student_criteria(self,min=0,max=100):
        return [x for x in data if x.get_avg()>min and x.get_avg()<max ]
				
import sys
if (__name__=="__main__"):
    if (len(sys.argv)!=5):
        pass
    else:
	
        stud_map=StudentMap(sys.argv[1])
        f2=open(sys.argv[4],"w")
        stud_map.mapfile()
		
        data = stud_map.student_list()	
        stud_cri=stud_map.student_criteria(int(sys.argv[2]),int(sys.argv[3]))
        stud_cri=stud_map.student_criteria(40,60)	
        f2.write(list(map(str,data)))
        f2.write(list(map(str,stud_cri)))
