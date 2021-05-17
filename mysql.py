import json
import pymysql


def generate_sql():
    data = {
        "title": "助理教授",
        "phone": "",
        "fax": "",
        "email": "cyy2020@hit.edu.cn",
        "field": "计算机视觉,机器学习,模式识别",
        "resume": "http://faculty.hitsz.edu.cn/chenyongyong",
        "name": "陈勇勇"
    }
    cols = ", ".join('`{}`'.format(k) for k in data.keys())
    val_cols = ', '.join('%({})s'.format(k) for k in data.keys())
    sql = """
     INSERT INTO teacher(%s) VALUES(%s)
     """ % (cols, val_cols)
    return sql


conn = pymysql.connect(host="localhost", user="root", password="123456", database="web")
print(conn.server_version)

cursor = conn.cursor()
sql = generate_sql()
print(sql)

with open("result.json","r") as f:
    dataList = json.load(f)
for i in dataList:
    cursor.execute(sql, i)
conn.commit()
cursor.close()

conn.close()
