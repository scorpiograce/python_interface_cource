from day3.day3_mysql import db_query,db_change

def check_user(name):
    r = db_query("select * from user where name='%s'" % name)
    if r:
      return True
    return False


# 删除用户
def del_user(name):
    db_change("delete from user where name='%s'" % name)

del_user("薛凌3")