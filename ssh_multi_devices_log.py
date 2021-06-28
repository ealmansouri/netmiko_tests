#!/usr/bin/env python
from netmiko import ConnectHandler


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

termLen = "term len 0"
showIpIntBrief = "show ip int brief"

contextList = ['local','OM_RC']

contextList2 = ['local','OM_RC','H_OSS','SS7','H_SIG','CN','SN','CH','H_PS_Access','H_CS_Access','H_PS_CN','H_Billing','RAN','H_ABIS','H_IUB','H_LTE','DCN','SIGN_LDAP','INTERNET','IAC','IGW','speedtest']

for device in (FWTSR01, FWTSR02):
    net_connect = ConnectHandler(**device)
    for x in (contextList):
        currentContext = x
        termLenCmd = net_connect.send_command(termLen)
        contextCmd = net_connect.send_command("context " + currentContext + " " + showIpIntBrief)
        showIntDescCmd = net_connect.send_command("show interface description")
    print(net_connect.find_prompt())
    net_connect.disconnect()


