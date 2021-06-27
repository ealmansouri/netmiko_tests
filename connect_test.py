#!/usr/bin/env python
from netmiko import ConnectHandler

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


FWTSR01 = {
    'device_type': 'ericsson_ipos',
    'host':   '10.202.51.231',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
}

term_len = "term len 0"
showIpIntBrief = "show ip int brief"
showContext = "show context all"


net_connect = ConnectHandler(**FWTSR01)
output = net_connect.send_command(term_len)
output = net_connect.send_command(showIpIntBrief)
output2 = net_connect.send_command(showContext)
print(output)
print(output2)
print(type(output2))

def Convert(output2):
    li = list(output2.split(" "))
    return li


#output2 = [x.strip(' ') for x in output2]
#print(output2)

print(Convert(output2))
#(Convert(output2)).replace(" ", "")
#print(output2)

# Show command that we execute
#term_len = "term len 0"
#command = "show ip int brief"
#for device2 in (FWTSR01, FWTSR02):
#    with ConnectHandler(**device2) as net_connect:
#        output = net_connect.send_command(term_len)
#        output = net_connect.send_command(command)
