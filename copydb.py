import pymysql
db =pymysql.connect(host = "localhost" , user = "root" , password = "123454321", db = "world")
if (__name__=='__main__'):

    cursor=db.cursor()
    cursor.execute("select ID, Name, CountryCode, District, Population from city")
    dataall = curor.fetchall()
    count=0

    for x in dataall:
        cursor.execute("insert into citydemo(id,name,ccode,district,pop) values({},{},{},{},{})".format(x[0],x[1,x[2,x[3],x[4]))
        count=count+1

    print("error")

    db.commit()
    print("no. o moves is {}".format(count))