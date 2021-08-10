#!/usr/bin/env python
from netmiko import ConnectHandler
import re
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException


ATN_BRAYGAH = {
    "device_type": "huawei",
    'host':   '10.155.201.131',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "ATN_BRAYGAH",
}

JALO_GPTC1_ATN = {
    "device_type": "huawei",
    'host':   '10.155.201.132',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "JALO_GPTC1_ATN",
}

RASLANUF = {
    "device_type": "huawei",
    'host':   '10.155.201.133',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "RASLANUF",
}

ZALAH_GPTC = {
    "device_type": "huawei",
    'host':   '10.155.201.134',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "ZALAH_GPTC",
}

TAHADEE = {
    "device_type": "huawei",
    'host':   '10.155.201.135',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "TAHADEE",
}

BEN_JAWAD_CENTER = {
    "device_type": "huawei",
    'host':   '10.155.201.136',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "BEN_JAWAD_CENTER",
}

ATN_NOFALIA = {
    "device_type": "huawei",
    'host':   '10.155.201.137',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "ATN_NOFALIA",
}

ZOLTEN = {
    "device_type": "huawei",
    'host':   '10.155.201.138',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "ZOLTEN",
}

JALU_KUFRA6 = {
    "device_type": "huawei",
    'host':   '10.155.201.139',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "JALU_KUFRA6",
}

MrradaGPTC = {
    "device_type": "huawei",
    'host':   '10.155.201.140',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "MrradaGPTC",
}

OJLA_GPTC = {
    "device_type": "huawei",
    'host':   '10.155.201.141',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "OJLA_GPTC",
}

KOFRA = {
    "device_type": "huawei",
    'host':   '10.155.201.142',
    'username': 'almadar',
    'password': 'Mrnd@123',
    "session_log": "KOFRA",
}

# Create a text file that we can write specific output to
outputFile = open("MPBNOutputHuawei2.csv","w")

# A list of each set of common VPRNs shared by different routers


# 
for device in (ATN_BRAYGAH, JALO_GPTC1_ATN, RASLANUF, ZALAH_GPTC, TAHADEE, BEN_JAWAD_CENTER, ATN_NOFALIA, ZOLTEN, JALU_KUFRA6, MrradaGPTC, OJLA_GPTC):
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
    screenLength = net_connect.send_command("screen-length 0 temporary")
    shIpIntBrief = net_connect.send_command("display ip int bri")
# Split the output from the "display ip int bri" into seperate lines
    outputArr = shIpIntBrief.splitlines()
# Create the headings within the CSV file created
    outputFile.write("Device" + "," + "Interface" + "," + "Subnet" + "," + "VRF" + "," + "Description" + "\n")
# Loop through each line according to the length of the variable Array as we don't know how many lines are in each output
    for i in range(len(outputArr)):
        # define a new variable for each line currently being processed with the loop (outputArr[i]) 
        # Regex matching the format of an IP address
        matchObj = re.search('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})(\/([0-9]{2,2}))', outputArr[i])
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
                intDesc = intDesc[12:]
            # 
            intVrf = net_connect.send_command("display current interface " + lineArr[0] + " | i vpn")
            if intVrf != "":
                intVrfName = intVrf.split()
            # write to the output file created earlier, to include the device name taken from the dictionary,
            # following by a colon, followed by the interface name , tab space then the IP address followed by a carriage return
            outputFile.write(str(deviceName) + "," + lineArr[0] + "," + lineArr[1] + "," + intVrfName[3] + "," + intDesc + "\n")
    print(net_connect.find_prompt())
    net_connect.disconnect()
# A loop to run the commands to extract the local IP's within each VPRNs routing table

