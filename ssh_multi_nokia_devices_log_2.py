#!/usr/bin/env python
from netmiko import ConnectHandler
import re

BEN_SR7_01 = {
    "device_type": 'nokia_sros',
    'host':   '10.202.129.1',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "BEN_SR7_01",
}

BEN_SR7_02 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.11',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "BEN_SR7_02",
}

FWT_SR7_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.7',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "FWT_SR7_01",
}

FWT_SR7_02 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.17',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "FWT_SR7_02",
}

HYM_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.9',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "HYM_SRA8_01",
}

ALM_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.2',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "ALM_SRA8_01",
}

ALB_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.3',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "ALB_SRA8_01",
}

DER_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.4',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "DER_SRA8_01",
}

DER_SRA8_02 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.14',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "DER_SRA8_02",
}

TOB_SRA8_01 = {
    "device_type": "nokia_sros",
    'host':   '10.202.129.5',
    'username': 'e.mansouri',
    'password': 'R0YgB1V!00',
    "session_log": "TOB_SRA8_01",
}

# Create a text file that we can write specific output to
outputFile = open("MPBNOutput.csv","w")

# A list of each set of common VPRNs shared by different routers

listBlue = ["30040", "30050", "30110", "30120", "30130", "30200", "30300", "30400"]
listRed = ["30040", "30050", "30060", "30200", "30300", "30400"]
listGreen = ["30010", "30020", "30030", "30040", "30050", "30060", "30110", "30120", "30130", "30200", "30300", "30400"]
listDer1 = ["30040", "30050", "30060", "30110", "30120", "30130", "30200", "30300", "30400"]
listDer2 = ["30040", "30110", "30120", "30130", "30200", "30300"]


# 
for device in (BEN_SR7_02, FWT_SR7_01, FWT_SR7_02):
    net_connect = ConnectHandler(**device)
# Store the hostname from the dictionary defined for each router
    deviceName = device["session_log"]
# Commands to be run to extract the local IP's within the global routing table
    termLenCmd = net_connect.send_command("environment no more")
    shRouteTable = net_connect.send_command("admin display-config")
# Split the output from the RIB into seperate lines
    outputArr = shRouteTable.splitlines()
# Loop through each line according to the length of the variable Array as we don't know how many lines are in each output
    for i in range(len(outputArr)):
        # define a new variable for each line currently being processed with the loop (outputArr[i]) 
        # Regex matching the format of an IP address
        matchObj = re.search(("address " + '([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})(\/([0-9]{2,2}))'), outputArr[i])
        print(matchObj)
        # If there is a match of an IP address within the line then;
        if matchObj:
            # create a variable array that is variable outputArr[i] split at each whitespace
            lineArr = matchObj
            # print the first array entry of the next line as the interface name is the first string on the following line
            # then a tab space followed by the first array entry of the current line which will be the IP address 
            print(outputArr[i+1].split()[0], "\t", lineArr[0])
            # write to the output file created earlier, to include the device name taken from the dictionary,
            # following by a colon, followed by the interface name , tab space then the IP address followed by a carriage return
            outputFile.write(str(deviceName) + "," + "0" + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
#### A loop to run the commands to extract the local IP's within each VPRNs routing table
###    for vprn in listBlue:
###        shRouteTable2 = net_connect.send_command("show router " + vprn + " route-table protocol local")
###        # Split the output from the RIB into seperate lines
###        outputArr = shRouteTable2.splitlines()
###        # Create a header within the output file to state the VPRN number above the RIB's output
###        #outputFile.write("\n--------------VPRN---------------:" + vprn + "\n")
###        for i in range(len(outputArr)):
###            matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###            if matchObj:
###                lineArr = outputArr[i].split()
###                print(outputArr[i+1].split()[0], "\t", lineArr[0])
###                outputFile.write(str(deviceName) + "," + vprn + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###    print(net_connect.find_prompt())
###    net_connect.disconnect()


###
###for device in (ALM_SRA8_01, ALB_SRA8_01, TOB_SRA8_01):
###    net_connect = ConnectHandler(**device)
###    deviceName = device["session_log"]
###    termLenCmd = net_connect.send_command("environment no more")
###    shRouteTable = net_connect.send_command("show router route-table protocol local")
###    outputArr = shRouteTable.splitlines()
#### Loop through each line according to the length of the variable Array as we don't know how many lines are in each output    
###    for i in range(len(outputArr)):
###        # define a new variable for each line currently being processed with the loop (outputArr[i]) 
###        # Regex matching the format of an IP address
###        matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###        # If there is a match of an IP address within the line then;
###        if matchObj:
###            # create a variable array that is variable outputArr[i] split at each whitespace
###            lineArr = outputArr[i].split()
###            # print the first array entry of the next line as the interface name is the first string on the following line
###            # then a tab space followed by the first array entry of the current line which will be the IP address 
###            print(outputArr[i+1].split()[0], "\t", lineArr[0])
###            # write to the output file created earlier, to include the device name taken from the dictionary,
###            # following by a colon, followed by the interface name , tab space then the IP address followed by a carriage return
###            outputFile.write(str(deviceName) + "," + "0" + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###    for vprn in listRed:
###        shRouteTable2 = net_connect.send_command("show router " + vprn + " route-table protocol local")
###        # Split the output from the RIB into seperate lines
###        outputArr = shRouteTable2.splitlines()
###        # Create a header within the output file to state the VPRN number above the RIB's output
###        #outputFile.write("\n--------------VPRN---------------:" + vprn + "\n")
###        for i in range(len(outputArr)):
###            matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###            if matchObj:
###                lineArr = outputArr[i].split()
###                print(outputArr[i+1].split()[0], "\t", lineArr[0])
###                outputFile.write(str(deviceName) + "," + vprn + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###    print(net_connect.find_prompt())
###    net_connect.disconnect()
###
###
###
###net_connect = ConnectHandler(**BEN_SR7_01)
###deviceName = BEN_SR7_01["session_log"]
###termLenCmd = net_connect.send_command("environment no more")
###shRouteTable = net_connect.send_command("show router route-table protocol local")
###outputArr = shRouteTable.splitlines()
#### Loop through each line according to the length of the variable Array as we don't know how many lines are in each output    
###for i in range(len(outputArr)):
###    # define a new variable for each line currently being processed with the loop (outputArr[i]) 
###    # Regex matching the format of an IP address
###    matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###    # If there is a match of an IP address within the line then;
###    if matchObj:
###        # create a variable array that is variable outputArr[i] split at each whitespace
###        lineArr = outputArr[i].split()
###        # print the first array entry of the next line as the interface name is the first string on the following line
###        # then a tab space followed by the first array entry of the current line which will be the IP address 
###        print(outputArr[i+1].split()[0], "\t", lineArr[0])
###        # write to the output file created earlier, to include the device name taken from the dictionary,
###        # following by a colon, followed by the interface name , tab space then the IP address followed by a carriage return
###        outputFile.write(str(deviceName) + "," + "0" + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###for vprn in listGreen:
###    shRouteTable2 = net_connect.send_command("show router " + vprn + " route-table protocol local")
###    # Split the output from the RIB into seperate lines
###    outputArr = shRouteTable2.splitlines()
###    # Create a header within the output file to state the VPRN number above the RIB's output
###    #outputFile.write("\n--------------VPRN---------------:" + vprn + "\n")
###    for i in range(len(outputArr)):
###        matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###        if matchObj:
###            lineArr = outputArr[i].split()
###            print(outputArr[i+1].split()[0], "\t", lineArr[0])
###            outputFile.write(str(deviceName) + "," + vprn + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###print(net_connect.find_prompt())
###net_connect.disconnect()
###
###
###
###net_connect = ConnectHandler(**DER_SRA8_01)
###deviceName = DER_SRA8_01["session_log"]
###termLenCmd = net_connect.send_command("environment no more")
###shRouteTable = net_connect.send_command("show router route-table protocol local")
###outputArr = shRouteTable.splitlines()
#### Loop through each line according to the length of the variable Array as we don't know how many lines are in each output    
###for i in range(len(outputArr)):
###    # define a new variable for each line currently being processed with the loop (outputArr[i]) 
###    # Regex matching the format of an IP address
###    matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###    # If there is a match of an IP address within the line then;
###    if matchObj:
###        # create a variable array that is variable outputArr[i] split at each whitespace
###        lineArr = outputArr[i].split()
###        # print the first array entry of the next line as the interface name is the first string on the following line
###        # then a tab space followed by the first array entry of the current line which will be the IP address 
###        print(outputArr[i+1].split()[0], "\t", lineArr[0])
###        # write to the output file created earlier, to include the device name taken from the dictionary,
###        # following by a colon, followed by the interface name , tab space then the IP address followed by a carriage return
###        outputFile.write(str(deviceName) + "," + "0" + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###for vprn in listDer1:
###    shRouteTable2 = net_connect.send_command("show router " + vprn + " route-table protocol local")
###    # Split the output from the RIB into seperate lines
###    outputArr = shRouteTable2.splitlines()
###    # Create a header within the output file to state the VPRN number above the RIB's output
###    #outputFile.write("\n--------------VPRN---------------:" + vprn + "\n")
###    for i in range(len(outputArr)):
###        matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###        if matchObj:
###            lineArr = outputArr[i].split()
###            print(outputArr[i+1].split()[0], "\t", lineArr[0])
###            outputFile.write(str(deviceName) + "," + vprn + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###print(net_connect.find_prompt())
###net_connect.disconnect()
###
###
###
###net_connect = ConnectHandler(**DER_SRA8_02)
###deviceName = DER_SRA8_02["session_log"]
###termLenCmd = net_connect.send_command("environment no more")
###shRouteTable = net_connect.send_command("show router route-table protocol local")
###outputArr = shRouteTable.splitlines()
#### Loop through each line according to the length of the variable Array as we don't know how many lines are in each output    
###for i in range(len(outputArr)):
###    # define a new variable for each line currently being processed with the loop (outputArr[i]) 
###    # Regex matching the format of an IP address
###    matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###    # If there is a match of an IP address within the line then;
###    if matchObj:
###        # create a variable array that is variable outputArr[i] split at each whitespace
###        lineArr = outputArr[i].split()
###        # print the first array entry of the next line as the interface name is the first string on the following line
###        # then a tab space followed by the first array entry of the current line which will be the IP address 
###        print(outputArr[i+1].split()[0], "\t", lineArr[0])
###        # write to the output file created earlier, to include the device name taken from the dictionary,
###        # following by a colon, followed by the interface name , tab space then the IP address followed by a carriage return
###        outputFile.write(str(deviceName) + "," + "0" + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###for vprn in listDer2:
###    shRouteTable2 = net_connect.send_command("show router " + vprn + " route-table protocol local")
###    # Split the output from the RIB into seperate lines
###    outputArr = shRouteTable2.splitlines()
###    # Create a header within the output file to state the VPRN number above the RIB's output
###    #outputFile.write("\n--------------VPRN---------------:" + vprn + "\n")
###    for i in range(len(outputArr)):
###        matchObj = re.match('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
###        if matchObj:
###            lineArr = outputArr[i].split()
###            print(outputArr[i+1].split()[0], "\t", lineArr[0])
###            outputFile.write(str(deviceName) + "," + vprn + "," + outputArr[i+1].split()[0] + "," + lineArr[0] + "\n")
###print(net_connect.find_prompt())
###net_connect.disconnect()
###
###
###
###