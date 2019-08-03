import pymysql
class City:
    def __init__(self,id,name,ccd,pop):
        self.id=id
        self.name=name
        self.ccd=ccd
        self.pop=pop

    def __str__(self):
        return "ID = {}  Name = {} Country Code = {} Population = {}".format(self.id,self.name,self.ccd,self.pop)

class CityMap:

    def __init__(self):
        self.db=pymysql.connect(host="local host",user="root",password="123454321",db="world")
        self.citylist=[]
        self.citylength=0

    def citymap(self):
        cursor=self.db.cursor()
        datalength=cursor.execute("select ID,Name,CountryCode,Pouplation from City")
        self.citylenght=datalength
        #file=open("database.csv","w")
        dataall=cursor.fetchall()
        for x in file:
            self.citylist.append(City(x[0] , x[1] , x[2], x[4]))
            print(list(map(str,citylist),"\n")

    def getlist(self):
        return self.citylist
    def getlength(self):
        return self.citylenght

    cm=citymap()
    cm.citymap()