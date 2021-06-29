#!/usr/bin/env python
from netmiko import ConnectHandler


BEN_SR7_01 = {
    "device_type": 'nokia_sros',
    'host':   '10.202.129.1',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "BEN_SR7_01.txt",
}

BEN_SR7_02 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.11',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "BEN_SR7_02.txt",
}

FWT_SR7_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.7',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "FWT_SR7_01.txt",
}

FWT_SR7_02 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.17',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "FWT_SR7_02.txt",
}

HYM_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.9',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "HYM_SRA8_01.txt",
}

ALM_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.2',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "ALM_SRA8_01.txt",
}

ALB_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.3',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "ALB_SRA8_01.txt",
}

DER_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.4',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "DER_SRA8_01.txt",
}

DER_SRA8_02 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.14',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "DER_SRA8_02.txt",
}

TOB_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.5',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "TOB_SRA8_01.txt",
}

val = input

listBlue = ["30040", "30050", "30110", "30120", "30130", "30200", "30300", "30400"]
listRed = ["30040", "30050", "30060", "30200", "30300", "30400"]
listGreen = ["30010", "30020", "30030", "30040", "30050", "30060", "30110", "30120", "30130", "30200", "30300", "30400"]
listDer1 = ["30040", "30050", "30060", "30110", "30120", "30130", "30200", "30300", "30400"]

listDer2 = ["30040", "30110", "30120", "30130", "30200", "30300"]

for device in (BEN_SR7_02, FWT_SR7_01, FWT_SR7_02):
    net_connect = ConnectHandler(**device)
    termLenCmd = net_connect.send_command("environment no more")
    shRouteTable = net_connect.send_command("show router route-table protocol local")
    for vprn in listBlue:
        shRouteTable2 = net_connect.send_command("show router " + vprn + " route-table protocol local")
    print(net_connect.find_prompt())
    net_connect.disconnect()

for device in (ALM_SRA8_01, ALB_SRA8_01, TOB_SRA8_01):
    net_connect = ConnectHandler(**device)
    termLenCmd = net_connect.send_command("environment no more")
    shRouteTable = net_connect.send_command("show router route-table protocol local")
    for vprn in listRed:
        shRouteTable = net_connect.send_command("show router " + vprn + " route-table protocol local")
    print(net_connect.find_prompt())
    net_connect.disconnect()
    
net_connect = ConnectHandler(**BEN_SR7_01)
termLenCmd = net_connect.send_command("environment no more")
shRouteTable = net_connect.send_command("show router route-table protocol local")
for vprn in listGreen:
    shRouteTable = net_connect.send_command("show router " + vprn + " route-table protocol local")
print(net_connect.find_prompt())
net_connect.disconnect()

net_connect = ConnectHandler(**DER_SRA8_01)
termLenCmd = net_connect.send_command("environment no more")
shRouteTable = net_connect.send_command("show router route-table protocol local")
for vprn in listDer1:
    shRouteTable = net_connect.send_command("show router " + vprn + " route-table protocol local")
print(net_connect.find_prompt())
net_connect.disconnect()

net_connect = ConnectHandler(**DER_SRA8_02)
termLenCmd = net_connect.send_command("environment no more")
shRouteTable = net_connect.send_command("show router route-table protocol local")
for vprn in listDer2:
    shRouteTable = net_connect.send_command("show router " + vprn + " route-table protocol local")
print(net_connect.find_prompt())
net_connect.disconnect()



