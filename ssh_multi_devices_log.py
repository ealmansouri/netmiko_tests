#!/usr/bin/env python
from netmiko import ConnectHandler


FWTSR01 = {
    'device_type': 'ericsson_ipos',
    'host':   '10.202.51.231',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "FWTSR01_output.txt",
}

FWTSR02 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.232',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "FWTSR02_output.txt",
}

BENSR01 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.225',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "BENSR01_output.txt",
}

BENSR02 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.226',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "BENSR02_output.txt",
}

DRNSE01 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.227',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "DRNSE01_output.txt",
}

DRNSE02 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.228',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "DRNSE02_output.txt",
}

EJISR01 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.235',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "EJISR01_output.txt",
}

EJISR02 = {
    "device_type": "ericsson_ipos",
    'host':   '10.202.51.236',
    'username': 'xxxxx',
    'password': 'xxxxx',
    "session_log": "EJISR02_output.txt",
}


termLen = "term len 0"
showIpIntBrief = "show ip int brief all-context"


for device in (FWTSR01, FWTSR02, BENSR01, BENSR02, DRNSE01, DRNSE02, EJISR01, EJISR02):
    net_connect = ConnectHandler(**device)
    termLenCmd = net_connect.send_command(termLen)
    shipintbriefCmd = net_connect.send_command(showIpIntBrief)
    print(net_connect.find_prompt())
    net_connect.disconnect()


