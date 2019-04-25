import pymysql
from datetime import datetime, date, timedelta
from chenhuan.grab3 import get_sorb


def storinfo(a):#１：需求　２：ｂｕｇ
    if len(get_sorb(a)) == 0:
        print("NO message!!")
    else:
        try:
            host = '数据库地址'
            user = 'root'
            password = '密码'
            db = 'storinfo'
            connection = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=db)
            cursor = connection.cursor()
            sql = "REPLACE INTO storinfo (ID,NRBM,CONTENT,PLANDATE,TPYE,FOUNDER,ASSIGNED) VALUES (%s,%s,%s,%s,%s,'null','null')"
            plandate = ((date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")).replace('-', '')
        except pymysql.Error as e:
            print("链接数据库失败：%s" % e)
        for xuhao, content in get_sorb(a).items():
            NRBM = xuhao
            ID = plandate + xuhao
            CONTENT = content
            values = (ID, NRBM, CONTENT, plandate, a)
            cursor.execute(sql, values)
            try:
                connection.commit()
            except:
                connection.rollback()
        connection.close()

storinfo(1)
storinfo(2)
