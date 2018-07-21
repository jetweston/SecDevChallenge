# SecDevChallenge


# Pre-conditions:

# Network Service ScanningDiscoveryT1046 (https://attack.mitre.org/wiki/Main_Page)

# TCP Rages:
# Ports 0 to 1023 are Well-Known Ports.
# Ports 1024 to 49151 are Registered Ports (often registered by a software developer to designate a particular port for their application)
# Ports 49152 to 65535 are Public Ports.

#!/usr/bin/env python
import socket
import subprocess
import sys


# Clear the screen
subprocess.call('clear', shell=True)


remoteServer = sys.argv[1]

remoteServerIP  = socket.gethostbyname(remoteServer)


print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)


# Scan all ports between 0 and 65535

try:
    for port in range(0,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}:  Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("Ctrl+C - Scan Terminated by User")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()


# Done Scanning.
print ('Scanning Completed')
