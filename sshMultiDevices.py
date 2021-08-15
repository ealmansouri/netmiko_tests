#!/usr/bin/env python


# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler


with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'admin',
            'password': 'cisco',
            'global_delay_factor': 3
        }
        routerIP = Router['ip']
        net_connect = ConnectHandler(**Router)
 
        print ('Connecting to ' + IP)
        print('-'*79)
        shIpIntBri = net_connect.send_command('sh ip int brief')
        hostnameCmd = net_connect.send_command('sh run | i hostname')
        hostnameList = hostnameCmd.split()
        hostname = hostnameList[1]
        print(shIpIntBri)
        print()
        print('-'*79)
        filename = (hostname + ".txt")
        logfile = open(filename, "a")
        logfile.write(hostname)
        logfile.write("\n")
        logfile.write('-'*79)
        logfile.write("\n")
        logfile.write(shIpIntBri)
        logfile.write("\n")
        logfile.write('-'*79)
        logfile.write("\n")
        # Finally close the connection
        net_connect.disconnect()