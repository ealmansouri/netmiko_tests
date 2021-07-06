#!/usr/bin/env python
from netmiko import ConnectHandler
import ipcalc


ipDict = {'10.155.112.50': '29', '10.155.112.51': '29', '10.155.113.50': '29', '10.155.113.51': '29', '10.155.114.50': '29', '10.155.114.51': '29', '10.155.114.58': '29', '10.155.114.59': '29', '10.155.114.66': '29', '10.155.114.67': '29', '10.155.115.50': '29', '10.155.115.58': '29', '10.155.115.59': '29', '10.155.122.186': '29', '10.155.122.187': '29', '10.155.122.194': '29', '10.155.122.195': '29', '10.155.122.202': '29', '10.155.122.203': '29', '10.155.122.50': '29', '10.155.122.51': '29', '10.155.122.58': '29', '10.155.122.59': '29', '10.155.122.66': '29', '10.155.122.67': '29', '10.155.123.194': '29', '10.155.123.195': '29', '10.155.123.202': '29', '10.155.123.203': '29', '10.155.123.66': '29', '10.155.123.67': '29', '10.155.123.74': '29', '10.155.123.75': '29', '10.155.123.82': '29', '10.155.123.83': '29', '10.155.123.90': '29', '10.155.123.91': '29', '10.155.124.106': '29', '10.155.124.107': '29', '10.155.124.114': '29', '10.155.124.115': '29', '10.155.124.122': '29', '10.155.124.123': '29', '10.155.124.98': '29', '10.155.124.99': '29', '10.155.125.50': '29', '10.155.125.51': '29', '10.155.125.58': '29', '10.155.125.59': '29', '10.155.125.66': '29', '10.155.125.67': '29', '10.155.125.74': '29', '10.155.125.75': '29', '10.155.126.50': '29', '10.155.126.58': '29', '10.155.126.59': '29', '10.155.129.10': '30', '10.155.129.14': '30', '10.155.129.50': '28', '10.155.131.173': '30', '10.155.14.129': '28', '10.155.14.145': '29', '10.155.16.1': '24', '10.155.17.1': '28', '10.155.17.105': '29', '10.155.17.113': '28', '10.155.17.129': '28', '10.155.17.145': '28', '10.155.17.17': '29', '10.155.17.25': '29', '10.155.17.33': '27', '10.155.17.65': '28', '10.155.17.81': '28', '10.155.170.181': '30', '10.155.170.185': '30', '10.155.170.189': '30', '10.155.170.22': '30', '10.155.171.173': '30', '10.155.171.181': '30', '10.155.171.185': '30', '10.155.171.189': '30', '10.155.171.193': '30', '10.155.171.197': '30', '10.155.171.201': '30', '10.155.171.22': '30', '10.155.172.173': '30', '10.155.172.22': '30', '10.155.173.181': '30', '10.155.173.185': '30', '10.155.173.189': '30', '10.155.173.22': '30', '10.155.18.1': '28', '10.155.18.113': '28', '10.155.18.17': '28', '10.155.18.177': '28', '10.155.18.193': '28', '10.155.18.33': '28', '10.155.18.49': '28', '10.155.18.97': '28', '10.155.19.1': '28', '10.155.19.129': '28', '10.155.19.145': '28', '10.155.19.161': '28', '10.155.19.17': '28', '10.155.19.177': '28', '10.155.19.193': '28', '10.155.19.209': '28', '10.155.19.33': '29', '10.155.19.41': '29', '10.155.19.49': '29', '10.155.19.57': '29', '10.155.19.65': '29', '10.155.197.1': '29', '10.155.197.129': '29', '10.155.198.9': '30', '10.155.20.1': '28', '10.155.20.113': '28', '10.155.20.129': '28', '10.155.20.145': '28', '10.155.20.161': '28', '10.155.20.17': '28', '10.155.20.177': '28', '10.155.20.193': '29', '10.155.20.209': '29', '10.155.20.217': '29', '10.155.20.65': '28', '10.155.20.81': '28', '10.155.20.97': '28', '10.155.200.129': '32', '10.155.200.130': '32', '10.155.201.129': '32', '10.155.201.130': '32', '10.155.204.1': '30', '10.155.204.106': '30', '10.155.204.110': '30', '10.155.204.113': '30', '10.155.204.118': '30', '10.155.204.122': '30', '10.155.204.126': '30', '10.155.204.134': '30', '10.155.204.137': '30', '10.155.204.138': '30', '10.155.204.14': '30', '10.155.204.141': '30', '10.155.204.142': '30', '10.155.204.2': '30', '10.155.204.253': '30', '10.155.204.37': '30', '10.155.204.42': '30', '10.155.204.46': '30', '10.155.204.5': '30', '10.155.204.50': '30', '10.155.204.54': '30', '10.155.204.58': '30', '10.155.204.62': '30', '10.155.204.66': '30', '10.155.204.70': '30', '10.155.204.82': '30', '10.155.204.86': '30', '10.155.204.9': '30', '10.155.204.90': '30', '10.155.204.94': '30', '10.155.21.1': '30', '10.155.21.13': '30', '10.155.21.21': '30', '10.155.21.25': '30', '10.155.21.33': '30', '10.155.21.37': '30', '10.155.21.45': '30', '10.155.21.49': '30', '10.155.21.57': '30', '10.155.21.61': '30', '10.155.21.69': '30', '10.155.21.73': '30', '10.155.21.81': '30', '10.155.21.9': '30', '10.155.235.189': '30', '10.155.235.193': '30', '10.155.235.197': '30', '10.155.235.201': '30', '10.155.235.205': '30', '10.155.235.209': '30', '10.155.235.213': '30', '10.155.235.217': '30', '10.155.235.217': '30', '10.155.235.221': '30', '10.155.235.225': '30', '10.155.235.225': '30', '10.155.235.229': '30', '10.155.235.233': '30', '10.155.235.237': '30', '10.155.235.241': '30', '10.155.240.14': '29', '10.155.254.1': '24', '10.155.255.254': '29', '10.155.255.254': '29', '10.155.29.30': '29', '10.155.30.14': '29', '10.155.30.22': '29', '10.155.30.222': '29', '10.155.30.238': '29', '10.155.30.246': '29', '10.155.30.254': '29', '10.155.30.30': '29', '10.155.30.38': '29', '10.155.30.6': '29', '10.155.31.126': '26', '10.155.31.190': '26', '10.155.31.222': '27', '10.155.31.254': '27', '10.155.31.62': '26', '10.155.42.1': '30', '10.155.42.101': '30', '10.155.42.109': '30', '10.155.42.113': '30', '10.155.42.117': '30', '10.155.42.13': '30', '10.155.42.145': '30', '10.155.42.17': '30', '10.155.42.173': '30', '10.155.42.177': '30', '10.155.42.21': '30', '10.155.42.25': '30', '10.155.42.29': '30', '10.155.42.37': '30', '10.155.42.41': '30', '10.155.42.45': '30', '10.155.42.49': '30', '10.155.42.5': '30', '10.155.42.53': '30', '10.155.42.57': '30', '10.155.42.61': '30', '10.155.42.65': '30', '10.155.42.69': '30', '10.155.42.73': '30', '10.155.42.77': '30', '10.155.42.81': '30', '10.155.42.85': '30', '10.155.42.89': '30', '10.155.42.9': '30', '10.155.42.93': '30', '10.155.42.97': '30', '10.155.44.49': '30', '10.155.45.25': '30', '10.155.57.1': '30', '10.155.57.101': '30', '10.155.57.109': '30', '10.155.57.113': '30', '10.155.57.117': '30', '10.155.57.13': '30', '10.155.57.145': '30', '10.155.57.17': '30', '10.155.57.173': '30', '10.155.57.177': '30', '10.155.57.21': '30', '10.155.57.25': '30', '10.155.57.29': '30', '10.155.57.37': '30', '10.155.57.41': '30', '10.155.57.45': '30', '10.155.57.49': '30', '10.155.57.5': '30', '10.155.57.53': '30', '10.155.57.57': '30', '10.155.57.61': '30', '10.155.57.65': '30', '10.155.57.69': '30', '10.155.57.73': '30', '10.155.57.77': '30', '10.155.57.81': '30', '10.155.57.85': '30', '10.155.57.89': '30', '10.155.57.9': '30', '10.155.57.93': '30', '10.155.57.97': '30', '10.155.59.49': '30', '10.155.60.25': '30', '10.155.72.1': '30', '10.155.72.101': '30', '10.155.72.109': '30', '10.155.72.113': '30', '10.155.72.117': '30', '10.155.72.13': '30', '10.155.72.145': '30', '10.155.72.17': '30', '10.155.72.173': '30', '10.155.72.177': '30', '10.155.72.21': '30', '10.155.72.25': '30', '10.155.72.29': '30', '10.155.72.37': '30', '10.155.72.41': '30', '10.155.72.45': '30', '10.155.72.49': '30', '10.155.72.5': '30', '10.155.72.53': '30', '10.155.72.57': '30', '10.155.72.61': '30', '10.155.72.65': '30', '10.155.72.69': '30', '10.155.72.73': '30', '10.155.72.77': '30', '10.155.72.81': '30', '10.155.72.85': '30', '10.155.72.89': '30', '10.155.72.9': '30', '10.155.72.93': '30', '10.155.72.97': '30', '10.155.74.49': '30', '10.155.75.25': '30', '10.155.87.1': '30', '10.155.87.101': '30', '10.155.87.109': '30', '10.155.87.113': '30', '10.155.87.117': '30', '10.155.87.13': '30', '10.155.87.145': '30', '10.155.87.17': '30', '10.155.87.173': '30', '10.155.87.177': '30', '10.155.87.21': '30', '10.155.87.25': '30', '10.155.87.29': '30', '10.155.87.37': '30', '10.155.87.41': '30', '10.155.87.45': '30', '10.155.87.49': '30', '10.155.87.5': '30', '10.155.87.53': '30', '10.155.87.57': '30', '10.155.87.61': '30', '10.155.87.65': '30', '10.155.87.69': '30', '10.155.87.73': '30', '10.155.87.77': '30', '10.155.87.81': '30', '10.155.87.85': '30', '10.155.87.89': '30', '10.155.87.9': '30', '10.155.87.93': '30', '10.155.87.97': '30', '10.155.89.49': '30', '10.155.90.25': '30', '10.158.103.205': '30', '10.158.103.245': '30', '10.158.107.41': '30', '10.158.107.5': '30', '10.158.117.205': '30', '10.158.117.245': '30', '10.158.121.41': '30', '10.158.121.5': '30', '10.158.130.245': '30', '10.158.134.41': '30', '10.158.134.5': '30', '10.158.146.205': '30', '10.158.146.245': '30', '10.158.150.41': '30', '10.158.150.5': '30', '10.158.255.185': '29', '10.158.255.193': '29', '10.158.255.201': '29', '10.158.255.245': '30', '10.158.255.249': '30', '10.158.255.253': '30', '10.158.255.57': '29', '10.158.255.65': '29', '10.158.255.73': '29', '10.158.28.101': '30', '10.158.28.105': '30', '10.158.28.109': '30', '10.158.28.113': '30', '10.158.28.117': '30', '10.158.28.121': '30', '10.158.28.129': '30', '10.158.28.133': '30', '10.158.28.137': '30', '10.158.28.141': '30', '10.158.28.145': '30', '10.158.28.149': '30', '10.158.28.153': '30', '10.158.28.157': '30', '10.158.28.161': '30', '10.158.28.169': '30', '10.158.28.173': '30', '10.158.28.177': '30', '10.158.28.181': '30', '10.158.28.185': '30', '10.158.28.193': '30', '10.158.28.197': '30', '10.158.28.233': '30', '10.158.28.53': '30', '10.158.28.57': '30', '10.158.28.61': '30', '10.158.28.65': '30', '10.158.28.69': '30', '10.158.28.73': '30', '10.158.28.77': '30', '10.158.28.85': '30', '10.158.28.89': '30', '10.158.28.93': '30', '10.158.28.97': '30', '10.158.29.233': '30', '10.158.29.241': '30', '10.158.31.10': '30', '10.158.31.101': '30', '10.158.31.6': '29', '10.158.31.73': '30', '10.158.59.17': '29', '10.158.61.133': '30', '128.81.207.158': '16', '128.81.207.194': '16', '172.30.5.77': '30', '192.168.0.1': '24', '192.168.0.2': '24', '192.168.101.201': '24', '192.168.143.1': '24', '192.168.3.1': '30', '192.168.3.1': '30'}

outputFile = open("networkAddresses.csv","w")

for key in ipDict:
#    print(key, '/', ipDict[key])
    subnet = ipcalc.Network("%s/%s" % (str(key), str(ipDict[key])))
#    print("The network address is: " + str(subnet.network()))
    outputFile.write(str(subnet.network()) + "\n")