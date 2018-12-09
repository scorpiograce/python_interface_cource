from suds.client import Client
import pymysql

service=Client("http://115.28.108.130:4000/?wsdl").service
result=service.addUser("范冰冰","123456")
print(result)