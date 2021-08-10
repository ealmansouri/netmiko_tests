#!/usr/bin/env python
from netmiko import ConnectHandler
import ipcalc


ipDict = {"10.155.197.17":"29", "10.155.42.137":"30", "10.155.42.141":"30", "10.155.42.149":"30", "10.155.42.153":"30", "10.155.42.157":"30", "10.155.42.161":"30", "10.155.42.165":"30", "10.155.42.169":"30", "10.155.42.33":"30", "10.155.42.181":"30", "10.155.171.65":"30", "10.155.171.97":"30", "10.155.42.105":"30", "10.155.42.201":"30", "10.155.170.197":"30", "10.155.57.137":"30", "10.155.57.141":"30", "10.155.57.149":"30", "10.155.57.153":"30", "10.155.57.157":"30", "10.155.57.161":"30", "10.155.57.165":"30", "10.155.57.169":"30", "10.155.57.33":"30", "10.155.57.181":"30", "10.155.172.65":"30", "10.155.172.101":"30", "10.155.57.105":"30", "10.155.57.201":"30", "10.155.171.213":"30", "10.155.72.137":"30", "10.155.72.141":"30", "10.155.72.149":"30", "10.155.72.153":"30", "10.155.72.157":"30", "10.155.72.161":"30", "10.155.72.165":"30", "10.155.72.169":"30", "10.155.72.33":"30", "10.155.72.181":"30", "10.155.174.65":"30", "10.155.174.97":"30", "10.155.72.105":"30", "10.155.72.201":"30", "10.155.171.209":"30", "10.155.87.137":"30", "10.155.87.141":"30", "10.155.87.149":"30", "10.155.87.153":"30", "10.155.87.157":"30", "10.155.87.161":"30", "10.155.87.165":"30", "10.155.87.169":"30", "10.155.87.33":"30", "10.155.87.181":"30", "10.155.131.65":"30", "10.155.131.125":"30", "10.155.87.105":"30", "10.155.87.201":"30", "10.155.173.197":"30", "10.158.29.253":"30", "10.158.29.237":"30", "10.158.29.245":"30", "10.158.29.249":"30", "10.158.28.1":"30", "10.158.28.5":"30", "10.158.28.13":"30", "10.155.236.9":"30", "10.158.28.17":"30", "10.158.31.81":"30", "10.158.31.109":"30", "10.158.28.189":"30", "10.158.28.21":"30", "10.158.31.77":"30", "10.155.193.41":"29", "10.155.43.13":"30", "10.158.105.93":"30", "10.155.58.13":"30", "10.158.119.93":"30", "10.155.73.13":"30", "10.158.132.93":"30", "10.155.88.13":"30", "10.158.148.93":"30", "10.158.29.217":"30", "10.158.31.25":"30", "10.158.40.153":"29", "192.168.0.1":"24", "10.155.201.131":"32", "128.83.224.249":"16", "10.155.197.33":"29", "10.155.43.37":"30", "10.155.43.45":"30", "10.155.43.49":"30", "10.155.43.53":"30", "10.155.43.57":"30", "10.155.43.61":"30", "10.155.43.65":"30", "10.155.43.69":"30", "10.155.43.73":"30", "10.155.43.77":"30", "10.158.106.197":"30", "10.158.102.137":"30", "10.155.43.101":"30", "10.155.43.105":"30", "10.155.43.109":"30", "10.155.43.121":"30", "10.155.43.125":"30", "10.155.43.129":"30", "10.155.45.17":"30", "10.158.107.9":"30", "10.155.170.18":"30", "10.155.58.37":"30", "10.155.58.45":"30", "10.155.58.49":"30", "10.155.58.53":"30", "10.155.58.57":"30", "10.155.58.61":"30", "10.155.58.65":"30", "10.155.58.69":"30", "10.155.58.73":"30", "10.155.58.77":"30", "10.158.120.197":"30", "10.158.116.137":"30", "10.155.58.101":"30", "10.155.58.105":"30", "10.155.58.109":"30", "10.155.58.121":"30", "10.155.58.125":"30", "10.155.58.129":"30", "10.155.60.17":"30", "10.158.121.9":"30", "10.155.171.18":"30", "10.155.73.37":"30", "10.155.73.45":"30", "10.155.73.49":"30", "10.155.73.53":"30", "10.155.73.57":"30", "10.155.73.61":"30", "10.155.73.65":"30", "10.155.73.69":"30", "10.155.73.73":"30", "10.155.73.77":"30", "10.158.133.197":"30", "10.158.129.138":"30", "10.155.73.97":"30", "10.155.73.101":"30", "10.155.73.105":"30", "10.155.73.109":"30", "10.155.73.121":"30", "10.155.73.125":"30", "10.155.73.129":"30", "10.155.75.17":"30", "10.158.134.9":"30", "10.155.172.18":"30", "10.155.88.37":"30", "10.155.88.45":"30", "10.155.88.49":"30", "10.155.88.53":"30", "10.155.88.57":"30", "10.155.88.61":"30", "10.155.88.65":"30", "10.155.88.69":"30", "10.155.88.73":"30", "10.155.88.77":"30", "10.158.149.197":"30", "10.158.145.137":"30", "10.155.88.101":"30", "10.155.88.105":"30", "10.155.88.109":"30", "10.155.88.121":"30", "10.155.88.125":"30", "10.155.88.129":"30", "10.155.90.17":"30", "10.158.150.9":"30", "10.155.173.18":"30", "10.158.29.129":"30", "10.158.29.121":"30", "10.158.29.125":"30", "10.158.29.133":"30", "10.158.29.145":"30", "10.158.29.149":"30", "10.158.29.153":"30", "10.158.29.185":"30", "10.158.29.189":"30", "10.158.29.193":"30", "10.158.29.205":"30", "10.158.29.137":"30", "10.158.29.141":"30", "10.158.29.105":"30", "192.168.0.2":"24", "10.155.201.132":"32", "128.83.224.187":"16", "10.155.197.81":"29", "10.155.45.1":"30", "10.155.45.5":"30", "10.155.45.9":"30", "10.155.45.13":"30", "10.155.45.21":"30", "10.155.45.29":"30", "10.155.45.33":"30", "10.155.45.37":"30", "10.155.45.41":"30", "10.155.45.45":"30", "10.155.45.49":"30", "10.155.170.193":"30", "10.155.60.1":"30", "10.155.60.5":"30", "10.155.60.9":"30", "10.155.60.13":"30", "10.155.60.21":"30", "10.155.60.29":"30", "10.155.60.33":"30", "10.155.60.37":"30", "10.155.60.41":"30", "10.155.60.45":"30", "10.155.60.49":"30", "10.155.171.193":"30", "10.155.75.1":"30", "10.155.75.5":"30", "10.155.75.9":"30", "10.155.75.13":"30", "10.155.75.21":"30", "10.155.75.29":"30", "10.155.75.33":"30", "10.155.75.37":"30", "10.155.75.41":"30", "10.155.75.45":"30", "10.155.75.49":"30", "10.155.171.205":"30", "10.155.90.1":"30", "10.155.90.5":"30", "10.155.90.9":"30", "10.155.90.13":"30", "10.155.90.21":"30", "10.155.90.29":"30", "10.155.90.33":"30", "10.155.90.37":"30", "10.155.90.41":"30", "10.155.90.45":"30", "10.155.90.49":"30", "10.155.173.193":"30", "10.158.30.101":"30", "10.158.30.81":"30", "10.158.30.85":"30", "10.158.30.93":"30", "10.158.30.97":"30", "10.158.30.121":"30", "10.158.30.117":"30", "192.168.0.3":"24", "10.155.201.133":"32", "128.83.224.163":"16", "10.155.197.97":"29", "10.155.45.97":"30", "10.155.45.101":"30", "10.155.45.105":"30", "10.155.45.109":"30", "10.155.45.113":"30", "10.155.45.117":"30", "10.155.45.121":"30", "10.155.45.125":"30", "10.155.45.129":"30", "10.155.45.133":"30", "10.155.45.137":"30", "10.155.45.141":"30", "10.155.45.145":"30", "10.155.45.149":"30", "10.155.45.153":"30", "10.155.45.157":"30", "10.158.103.113":"30", "10.158.103.117":"30", "10.158.107.13":"30", "10.158.107.17":"30", "10.158.107.21":"30", "10.155.60.97":"30", "10.155.60.101":"30", "10.155.60.105":"30", "10.155.60.109":"30", "10.155.60.113":"30", "10.155.60.117":"30", "10.155.60.121":"30", "10.155.60.125":"30", "10.155.60.129":"30", "10.155.60.133":"30", "10.155.60.137":"30", "10.155.60.141":"30", "10.155.60.145":"30", "10.155.60.149":"30", "10.155.60.153":"30", "10.155.60.157":"30", "10.158.117.113":"30", "10.158.117.117":"30", "10.158.121.13":"30", "10.158.121.17":"30", "10.158.121.21":"30", "10.155.75.97":"30", "10.155.75.101":"30", "10.155.75.105":"30", "10.155.75.109":"30", "10.155.75.113":"30", "10.155.75.117":"30", "10.155.75.121":"30", "10.155.75.125":"30", "10.155.75.129":"30", "10.155.75.133":"30", "10.155.75.137":"30", "10.155.75.141":"30", "10.155.75.145":"30", "10.155.75.149":"30", "10.155.75.153":"30", "10.155.75.157":"30", "10.158.134.13":"30", "10.158.134.17":"30", "10.158.134.21":"30", "10.155.90.97":"30", "10.155.90.101":"30", "10.155.90.105":"30", "10.155.90.109":"30", "10.155.90.113":"30", "10.155.90.117":"30", "10.155.90.121":"30", "10.155.90.125":"30", "10.155.90.129":"30", "10.155.90.133":"30", "10.155.90.137":"30", "10.155.90.141":"30", "10.155.90.145":"30", "10.155.90.149":"30", "10.155.90.153":"30", "10.155.90.157":"30", "10.158.146.113":"30", "10.158.146.117":"30", "10.158.150.13":"30", "10.158.150.17":"30", "10.158.150.21":"30", "10.158.30.45":"30", "10.158.30.41":"30", "10.158.30.53":"30", "10.158.31.113":"30", "10.158.31.117":"30", "10.158.30.49":"30", "10.158.30.37":"30", "10.158.30.29":"30", "192.168.0.5":"24", "10.155.201.134":"32", "128.83.224.225":"16", "10.155.197.9":"29", "10.155.42.121":"30", "10.155.42.125":"30", "10.155.42.129":"30", "10.155.42.133":"30", "10.155.170.30":"30", "10.155.57.121":"30", "10.155.57.125":"30", "10.155.57.129":"30", "10.155.57.133":"30", "10.155.171.30":"30", "10.155.72.121":"30", "10.155.72.125":"30", "10.155.72.129":"30", "10.155.72.133":"30", "10.155.172.30":"30", "10.155.87.121":"30", "10.155.87.125":"30", "10.155.87.129":"30", "10.155.87.133":"30", "10.155.173.30":"30", "10.158.28.25":"30", "10.158.28.29":"30", "10.158.28.33":"30", "10.158.28.37":"30", "10.158.28.41":"30", "192.168.0.6":"24", "10.155.201.136":"32", "128.83.224.195":"16", "10.155.197.65":"29", "10.155.44.121":"30", "10.155.44.125":"30", "10.155.44.129":"30", "10.155.44.133":"30", "10.155.44.137":"30", "10.155.44.141":"30", "10.155.44.145":"30", "10.155.44.149":"30", "10.155.170.130":"30", "10.158.103.237":"30", "10.155.59.121":"30", "10.155.59.125":"30", "10.155.59.129":"30", "10.155.59.133":"30", "10.155.59.137":"30", "10.155.59.141":"30", "10.155.59.145":"30", "10.155.59.149":"30", "10.155.171.130":"30", "10.158.117.237":"30", "10.155.74.121":"30", "10.155.74.125":"30", "10.155.74.129":"30", "10.155.74.133":"30", "10.155.74.137":"30", "10.155.74.141":"30", "10.155.74.145":"30", "10.155.74.149":"30", "10.155.172.130":"30", "10.158.130.237":"30", "10.155.89.121":"30", "10.155.89.125":"30", "10.155.89.129":"30", "10.155.89.133":"30", "10.155.89.137":"30", "10.155.89.141":"30", "10.155.89.145":"30", "10.155.89.149":"30", "10.155.173.130":"30", "10.158.146.237":"30", "10.158.30.209":"30", "10.158.30.181":"30", "10.158.30.185":"30", "10.158.30.189":"30", "10.158.30.205":"30", "10.158.30.213":"30", "10.158.30.197":"30", "10.158.30.193":"30", "10.158.30.201":"30", "10.158.31.85":"30", "192.168.0.7":"24", "10.155.201.137":"32", "128.83.224.165":"16", "10.155.197.105":"29", "10.155.45.161":"30", "10.155.60.161":"30", "10.155.75.161":"30", "10.155.90.161":"30", "10.158.30.17":"30", "192.168.0.8":"24", "10.155.201.138":"32", "128.83.224.235":"16", "10.155.43.137":"30", "10.155.43.141":"30", "10.155.43.149":"30", "10.155.43.153":"30", "10.155.43.157":"30", "10.155.43.161":"30", "10.155.43.165":"30", "10.155.43.169":"30", "10.155.43.173":"30", "10.155.171.109":"30", "10.155.58.137":"30", "10.155.58.141":"30", "10.155.58.149":"30", "10.155.58.153":"30", "10.155.58.157":"30", "10.155.58.161":"30", "10.155.58.165":"30", "10.155.58.169":"30", "10.155.58.173":"30", "10.155.172.113":"30", "10.155.73.137":"30", "10.155.73.141":"30", "10.155.73.149":"30", "10.155.73.153":"30", "10.155.73.157":"30", "10.155.73.161":"30", "10.155.73.165":"30", "10.155.73.169":"30", "10.155.73.173":"30", "10.155.174.109":"30", "10.155.88.137":"30", "10.155.88.149":"30", "10.155.88.153":"30", "10.155.88.157":"30", "10.155.88.161":"30", "10.155.88.165":"30", "10.155.88.169":"30", "10.155.88.173":"30", "10.155.131.105":"30", "10.155.236.13":"30", "10.158.29.101":"30", "10.158.29.97":"30", "10.158.40.17":"30", "10.155.197.89":"29", "10.155.45.53":"30", "10.155.45.57":"30", "10.155.45.61":"30", "10.155.45.65":"30", "10.155.45.69":"30", "10.155.45.73":"30", "10.155.45.77":"30", "10.155.45.81":"30", "10.155.45.85":"30", "10.155.45.89":"30", "10.155.45.93":"30", "10.155.170.58":"30", "10.155.170.62":"30", "10.155.60.53":"30", "10.155.60.57":"30", "10.155.60.61":"30", "10.155.60.65":"30", "10.155.60.69":"30", "10.155.60.73":"30", "10.155.60.77":"30", "10.155.60.81":"30", "10.155.60.85":"30", "10.155.60.89":"30", "10.155.60.93":"30", "10.155.171.58":"30", "10.155.171.62":"30", "10.155.75.53":"30", "10.155.75.57":"30", "10.155.75.61":"30", "10.155.75.65":"30", "10.155.75.69":"30", "10.155.75.73":"30", "10.155.75.77":"30", "10.155.75.81":"30", "10.155.75.85":"30", "10.155.75.89":"30", "10.155.75.93":"30", "10.155.172.58":"30", "10.155.172.62":"30", "10.155.90.53":"30", "10.155.90.57":"30", "10.155.90.61":"30", "10.155.90.65":"30", "10.155.90.69":"30", "10.155.90.73":"30", "10.155.90.77":"30", "10.155.90.81":"30", "10.155.90.85":"30", "10.155.90.89":"30", "10.155.90.93":"30", "10.155.173.58":"30", "10.155.173.62":"30", "10.158.30.73":"30", "10.158.30.57":"30", "10.155.236.17":"30", "10.158.30.77":"30", "10.158.30.65":"30", "10.158.30.69":"30", "10.155.43.145":"30", "10.155.58.145":"30", "10.155.73.145":"30", "10.155.88.145":"30", "10.158.29.73":"30", "10.158.29.117":"30", "10.158.40.57":"30", "10.155.88.141":"30", "192.168.0.9":"24", "10.155.43.133":"30", "10.155.58.133":"30", "10.155.73.133":"30", "10.155.88.133":"30", "10.155.201.139":"32", "128.83.224.167":"16", "10.155.197.57":"29", "10.155.44.85":"30", "10.155.44.89":"30", "10.155.44.93":"30", "10.155.44.97":"30", "10.155.44.101":"30", "10.155.44.105":"30", "10.155.44.109":"30", "10.155.44.113":"30", "10.155.44.117":"30", "10.155.59.85":"30", "10.155.59.89":"30", "10.155.59.93":"30", "10.155.59.97":"30", "10.155.59.101":"30", "10.155.59.105":"30", "10.155.59.109":"30", "10.155.59.113":"30", "10.155.59.117":"30", "10.155.74.85":"30", "10.155.74.89":"30", "10.155.74.93":"30", "10.155.74.97":"30", "10.155.74.101":"30", "10.155.74.105":"30", "10.155.74.109":"30", "10.155.74.113":"30", "10.155.74.117":"30", "10.155.89.85":"30", "10.155.89.89":"30", "10.155.89.93":"30", "10.155.89.97":"30", "10.155.89.101":"30", "10.155.89.105":"30", "10.155.89.109":"30", "10.155.89.113":"30", "10.155.89.117":"30", "10.158.30.225":"30", "10.158.30.221":"30", "10.158.30.229":"30", "10.155.45.165":"30", "10.155.45.185":"30", "10.155.45.189":"30", "10.155.45.193":"30", "10.155.45.197":"30", "10.155.45.201":"30", "10.155.45.205":"30", "10.155.60.165":"30", "10.155.60.185":"30", "10.155.60.189":"30", "10.155.60.193":"30", "10.155.60.197":"30", "10.155.60.201":"30", "10.155.60.205":"30", "10.155.75.165":"30", "10.155.75.185":"30", "10.155.75.189":"30", "10.155.75.193":"30", "10.155.75.197":"30", "10.155.75.201":"30", "10.155.75.205":"30", "10.155.90.165":"30", "10.155.90.185":"30", "10.155.90.189":"30", "10.155.90.193":"30", "10.155.90.197":"30", "10.155.90.201":"30", "10.155.90.205":"30", "10.158.30.217":"30", "10.158.28.45":"30", "10.155.210.25":"29", "192.168.0.10":"24", "10.155.201.140":"32", "128.83.224.133":"16", "172.30.1.237":"30", "10.155.197.73":"29", "10.155.44.153":"30", "10.155.44.157":"30", "10.155.44.161":"30", "10.155.44.165":"30", "10.155.44.169":"30", "10.155.44.173":"30", "10.155.44.177":"30", "10.155.44.181":"30", "10.155.44.185":"30", "10.155.44.189":"30", "10.155.44.193":"30", "10.155.44.197":"30", "10.155.44.201":"30", "10.155.44.69":"30", "10.155.59.153":"30", "10.155.59.157":"30", "10.155.59.161":"30", "10.155.59.165":"30", "10.155.59.169":"30", "10.155.59.173":"30", "10.155.59.177":"30", "10.155.59.181":"30", "10.155.59.185":"30", "10.155.59.189":"30", "10.155.59.193":"30", "10.155.59.197":"30", "10.155.59.201":"30", "10.155.59.69":"30", "10.155.74.153":"30", "10.155.74.157":"30", "10.155.74.161":"30", "10.155.74.165":"30", "10.155.74.169":"30", "10.155.74.173":"30", "10.155.74.177":"30", "10.155.74.181":"30", "10.155.74.185":"30", "10.155.74.189":"30", "10.155.74.193":"30", "10.155.74.197":"30", "10.155.74.201":"30", "10.155.74.69":"30", "10.155.89.153":"30", "10.155.89.157":"30", "10.155.89.161":"30", "10.155.89.165":"30", "10.155.89.169":"30", "10.155.89.173":"30", "10.155.89.177":"30", "10.155.89.181":"30", "10.155.89.185":"30", "10.155.89.189":"30", "10.155.89.193":"30", "10.155.89.197":"30", "10.155.89.201":"30", "10.155.89.69":"30", "10.158.30.169":"30", "10.158.30.125":"30", "10.158.30.129":"30", "10.158.30.133":"30", "10.158.30.157":"30", "10.158.30.161":"30", "10.158.30.165":"30", "10.158.30.173":"30", "10.158.30.177":"30", "192.168.0.11":"24", "10.155.201.141":"32", "128.83.225.91":"16"}

outputFile = open("networkAddressesHuawei2.csv","w")

for key in ipDict:
    print(key, '/', ipDict[key])
    subnet = ipcalc.Network("%s/%s" % (str(key), str(ipDict[key])))
    print("The network address is: " + str(subnet.network()))
    outputFile.write(str(subnet.network()) + "\n")