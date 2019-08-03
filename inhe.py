class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    def getroll(self):
        return self.roll

    def getname(self):
        return self.name
    def __str__(self):
        return "Super Class"

class PHD(Student):
    def __init__(self,roll,name,sal):
        super().__init__(roll,name)
        self.sal=sal

    def print_detail(self):
        print(self.__str__())
        print(super().__str__())
        print(str(super().getroll()) + "  " + super().getname())


    def __str__(self):
        return "Sub Class"

p=PHD(78,"shreyas",25000)
p.print_detail()