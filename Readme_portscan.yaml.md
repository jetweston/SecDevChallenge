## SecDevChallenge

### Exploit T1046: Network Service Scanning & Discovery 

Network Service Scanning:	Discovery:	T1046	Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information include port scans and vulnerability scans using tools that are brought onto a system (reference: https://attack.mitre.org/wiki/Main_Page)

### Pre-conditions:

- Operating System: 
  Darwin xanax.local 17.7.0 Darwin Kernel Version 17.7.0: Thu Jun 21 22:53:14 PDT 2018; root:xnu-4570.71.2~1/RELEASE_X86_64 x86_64 


- Ansible: 
  version 2.3.1.0
  python version = 2.7.13 (default, Dec 18 2016, 07:03:39) [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]
  
  - nmap:
    For the sake of brevity we will use 'nmap -F' which scans the top 100 most common ports 
    Use 'nmap -p- ' to scannal all 65535 ports nsise scan.
  
  
 ### Execution of the attack

SCAN TCP Rages:
Ports 0 to 1023 are Well-Known Ports.
Ports 1024 to 49151 are Registered Ports (often registered by a software developer to designate a particular port for their application)
Ports 49152 to 65535 are Public Ports.

Usage:
 - get clone
 - /usr/local/bin/ansible-playbook portscan.yaml
  


### Postconditions
  
  
  

