import json
import requests
from pyzabbix import ZabbixAPI


#api_address="http://192.168.56.102/zabbix/api_jsonrpc.php"
api_address=raw_input("enter correct URL to api_jsonrpc.php, like http://192.168.56.102/zabbix/api_jsonrpc.php"": \n")
zbx_sessionid= raw_input("enter zbx_sessionid: \n")
user= raw_input("enter username: \n")
password= raw_input("enter password: \n")

url = api_address
headers = {'Content-type': 'application/json'}
data = {"jsonrpc": "2.0", "method": "user.create", "params": {
    "alias": user, "passwd": password, "type": "3", "usrgrps": [
        {"usrgrpid": "7"}], },
        "auth": zbx_sessionid,
        "id": 1
        }
answer = requests.post(url, data=json.dumps(data), headers=headers)
print(answer)
response = answer.json()
print(response)
print ("testing user parameters:")
zapi = ZabbixAPI(api_address)
zapi.login(user, password)
print("Connected to Zabbix API Version %s" % zapi.api_version())
# data = {"jsonrpc": "2.0", "method": "user.login", "params": {
#     "user": user, "passwd": password },
#         "auth": None,
#         "id": 1
#         }
# answer = requests.post(url, data=json.dumps(data), headers=headers)
# print(answer)
# response = answer.json()
# print(response)
