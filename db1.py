import pymysql
class City:
    def __init__(self,id,name,ccd,dis,pop):
        self.id=id
        self.name=name
        self.ccd=ccd
        self.dis=dis
        self.pop=pop

    def __str__(self):
        return "ID = {}  Name = {} Country Code = {} District = {} Population = {}".format(self.id,self.name,self.ccd,self.dis,self.pop)

class CityMap:

    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="123454321",db="world")
        self.citylist=[]
        self.citylength=0

    def cityMap(self):
        cursor=self.db.cursor()
        datalength = cursor.execute("select ID,Name,CountryCode,District,Population from city")
        self.citylength = datalength
        file=open("database.csv","w")
        dataall=cursor.fetchall()
        for x in dataall:
            self.citylist.append(City(x[0] , x[1] , x[2], x[3], x[4]))
            file.write(",".join(list(map(ascii,x))) + "\n")

        print(list(map(str,self.getlist())))


        print(self.getlength())
    def getlist(self):
        return self.citylist

    def getlength(self):
        return self.citylength

cm = CityMap()
cm.cityMap()
