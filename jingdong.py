import re
import json
import requests
import pymysql

db=pymysql.connect("localhost","root","123456","django",charset="utf8")
cursor=db.cursor()

pid=[100000177774,100004169710,8051104,8264407,7120000,6735790,7651951,100000400012]
for i in pid:
    response=requests.get(url='https://p.3.cn/prices/mgets?skuIds={}'.format(i))
    price_json=response.json()
    id=price_json[0]['id']
    maxprice=price_json[0]['m']
    opprice=price_json[0]['op']
    pprice=price_json[0]['p']
    sql = "insert into web_phoneprice(id,maxprice,opprice,pprice) values('{}',{},{},{})".format(id,maxprice,opprice,pprice)
    cursor.execute(sql)
    db.commit()
db.close()