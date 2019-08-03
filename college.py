
class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    def getroll(self):
        return self.roll

    def getname(self):
        return self.name

class College:
    def __init__(self):
        self.python=[]
        self.java=[]

    def admitstudent(self,course,student):
        if (course == "python"):
            self.python.append(student)

        elif (course == "java"):
            self.java.append(student)

    def print_detail(self,course):
        if ( course == "python"):
            for x in self.python:
                print(x.getname() + "   " + str(x.getroll()))

        if (course == "java"):
            for x in self.java:
                print(x.getname() + "   " + str(x.getroll()))


st1=Student(1,"shreyas")
st2=Student(2,"anamika")
st3=Student(3,"vivek")

c=College()
c.admitstudent("python",st1)
c.admitstudent("java",st2)
c.admitstudent("python",st3)

c.print_detail("python")
print("\n\n")
c.print_detail("java")