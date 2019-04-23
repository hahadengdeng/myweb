import requests
from lxml import etree
import pymysql

def mystring(p):
    q=str(p)
    q=q.replace(' ','')
    q=q.replace('\\n','')
    q=q.replace('[','')
    q=q.replace(']','')
    q=q.replace('\'','')
    q=q.replace('\"','')
    q=q.replace(',','')
    return q

db=pymysql.connect("localhost","root","123456","django",charset="utf8")
cursor=db.cursor()

for page in range(0,10):
    url='https://movie.douban.com/top250?start={}&filter='.format(page*25)
    r=requests.get(url).text
    s=etree.HTML(r)
    for id in range(0,25):
       # print(mystring(s.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]/text()'.format(id+1))))     
        name=mystring(s.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]/text()'.format(id+1)))
        sql2="insert into web_movie(moviename) values('{}')".format(name)
        cursor.execute(sql2)
        db.commit()
db.close()            
