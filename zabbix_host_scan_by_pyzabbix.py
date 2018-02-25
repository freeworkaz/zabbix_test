import ast
from pyzabbix import ZabbixAPI

api_address=raw_input("enter correct URL to api_jsonrpc.php, like http://192.168.56.102/zabbix/api_jsonrpc.php"": \n")
#zbx_sessionid= raw_input("enter zbx_sessionid: \n")
user= raw_input("enter username: \n")
password= raw_input("enter password: \n")

zapi = ZabbixAPI(api_address)
zapi.login(user, password)
print("Connected to Zabbix API Version %s" % zapi.api_version())

for h in zapi.host.get(output="extend"):
    hostid=h['hostid']
    host=h['host']
    print ("found host: ",host,"hostid: ",hostid)  
