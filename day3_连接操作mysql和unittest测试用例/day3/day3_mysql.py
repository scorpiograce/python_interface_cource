import pymysql
"""
# 1 建立连接
conn=pymysql.connect(host='115.28.108.130',
                     port=3306,
                     user='test',
                     password='123456',
                     db='api_test',
                     charset='utf8')
# 2 从连接建立操作游标
cur=conn.cursor()
# 3 用游标执行查询/修改sql语句(游标是数据库的操作符，指向缓冲区)
cur.execute("select * from user where name='xue'")
# 4 获取查询结果
r= cur.fetchone()  #查询一条
#r2=cur.fetchall()  #(按顺序从除之前已查出的以外的剩余的里)查询所有记录
#r3=cur.fetchmany(3)  #(按顺序从除之前已查出的以外的剩余的里)查询指定数量条的记录
print(r)
#print(r2)
#print(r3)
# 5 关闭游标和连接
cur.close()
conn.close()
"""
"""
# 查询不同姓名的
conn=pymysql.connect(host='115.28.108.130',
                     port=3306,
                     user='test',
                     password='123456',
                     db='api_test',
                     charset='utf8')
name="xue"
sql="select * from user where name = '%s'" %name  # 查询不同姓名的
print(sql)
cur=conn.cursor()
cur.execute(sql)
r=cur.fetchone()
print(r)
"""

# 练习：
# 封装一个获取连接的函数
# 封装一个执行数据库查询的函数，返回所有结果
# 封装一个修改数据库的函数

name="xue"
sql="select * from user where name = '%s'" %name

def get_conn():
    conn=pymysql.connect(host='115.28.108.130',
                     port=3306,
                     user='test',
                     password='123456',
                     db='api_test',
                     charset='utf8')
    return conn

def db_query(sql):
    c=get_conn()
    cur=c.cursor()
    cur.execute(sql)
    r=cur.fetchall()
    cur.close()
    c.close()
    return r

sql2="update user set name='xue2' where name ='xue' limit 1"
sql3="select * from user where name='xue2'"

def db_change(sql2):
    c=get_conn()
    cur=c.cursor()
    cur.execute(sql2)
    r=cur.fetchall()
    cur.close()
    c.close()

print(db_query(sql))
print(db_query(sql3))
