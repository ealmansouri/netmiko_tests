#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

FWTSR01 = {
    'device_type': 'ericsson_ipos',
    'host':   '10.202.51.231',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "FWTSR01_output.txt",
}

FWTSR02 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.231',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "FWTSR02_output.txt",
}


for device in (FWTSR01, FWTSR02):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(term_len)
    output = net_connect.send_command(command)
    print(net_connect.find_prompt())
    net_connect.disconnect()


# Show command that we execute
#term_len = "term len 0"
#command = "show ip int brief"
#for device2 in (FWTSR01, FWTSR02):
#    with ConnectHandler(**device2) as net_connect:
#        output = net_connect.send_command(term_len)
#        output = net_connect.send_command(command)
