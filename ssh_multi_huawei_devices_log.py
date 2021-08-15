#!/usr/bin/env python
from netmiko import ConnectHandler
import re
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException



BGZ_CE12804S_EOR = {
    "device_type": 'huawei',
    'host':   '10.155.16.1',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "BGZ_CE12804S_EOR",
}

CX_Jdabia01 = {
    "device_type": "huawei",
    'host':   '10.155.201.129',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "CX_Jdabia01",
}

CX_Jdabia02 = {
    "device_type": "huawei",
    'host':   '10.155.201.130',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "CX_Jdabia02",
}


# Create a text file that we can write specific output to
outputFile = open("MPBNOutputHuaweiNew.csv","w")

# A list of each set of common VPRNs shared by different routers


# 
for device in (BGZ_CE12804S_EOR, CX_Jdabia01, CX_Jdabia02):
#for device in (CX_Jdabia01, BGZ_CE12804S_EOR):
    deviceName = device["session_log"]
    try:
        net_connect = ConnectHandler(**device)
    except (AuthenticationException):
        print("Authetication failure: " + str(deviceName))
        continue
    except (NetMikoTimeoutException):
        print("Time out from device: " + str(deviceName))
        continue
    except (SSHException):
        print("Not able to SSH: Try with Telnet:  " + str(deviceName))
        continue
    except Exception as unknown_error:
        print("other: " + unknown_error)
        continue
# Store the hostname from the dictionary defined for each router
# Commands to be run to extract the local IP's within the global routing table
    termLenCmd = net_connect.send_command("N\n")
    shRouteTable = net_connect.send_command("display ip int bri | no-more")
# Split the output from the "display ip int bri" into seperate lines
    outputArr = shRouteTable.splitlines()
# Loop through each line according to the length of the variable Array as we don't know how many lines are in each output
    outputFile.write("Device" + "," + "Interface" + "," + "Subnet" + "," + "VRF" + "," + "Description" + "\n")
    for i in range(len(outputArr)):
        # define a new variable for each line currently being processed with the loop (outputArr[i]) 
        # Regex matching the format of an IP address
        matchObj = re.search('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', outputArr[i])
        # If there is a match of an IP address within the line then;
        if matchObj:
            # create a variable array that is variable outputArr[i] split at each whitespace
            lineArr = outputArr[i].split()
            # Collect the interface description from the current config of the interface
            intDesc = net_connect.send_command("display current interface " + lineArr[0] + " | i description")
            # Deal with the CLI output that occurs beginning with "Info:"
            if intDesc[0:5] == "Info:":
            # Collect the description that occurs on the 137'th character of the CLI
                intDesc = intDesc[137:]
            # If there is no additional line of text beginning with "Info:", collect the description that begins at the 13th character
            if intDesc != "":
                intDesc = intDesc[13:]
            # 
            intVrf = net_connect.send_command("display current interface " + lineArr[0] + " | i vpn")
            intVrfName = intVrf.split()
            if intVrf[0:5] == "Info:":
                intVrf = intVrf[137:]
            if intVrf != "":
                intVrf = intVrf[25:]
            # write to the output file created earlier, to include the device name taken from the dictionary,
            # following by a colon, followed by the interface name , tab space then the IP address followed by a carriage return
            outputFile.write(str(deviceName) + "," + lineArr[0] + "," + lineArr[1] + "," + intVrf + "," + intDesc + "\n")
    print(net_connect.find_prompt())
    net_connect.disconnect()
# A loop to run the commands to extract the local IP's within each VPRNs routing table

