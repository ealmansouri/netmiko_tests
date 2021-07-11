#!/usr/bin/env python
from netmiko import ConnectHandler
import ipcalc

address = "10.155.30.238"
mask = 29

#outputFile = open("test.csv","w")

# for key in ipDict:
#    print(key, '/', ipDict[key])
subnet = ipcalc.Network("%s/%d" % (address, mask))
print(address + "/" + str(mask))
print("The network address is: " + str(subnet.network()))
#outputFile.write(str(subnet.network()) + "\n")
