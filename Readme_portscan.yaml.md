## SecDevChallenge

### Exploit T1046: Network Service Scanning & Discovery 

Network Service Scanning:	Discovery:	T1046	Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information include port scans and vulnerability scans using tools that are brought onto a system (reference: https://attack.mitre.org/wiki/Main_Page)

Port TCP Rages:
Ports 0 to 1023 are Well-Known Ports.
Ports 1024 to 49151 are Registered Ports (often registered by a software developer to designate a particular port for their application)
Ports 49152 to 65535 are Public Ports.

### Pre-conditions:


- 
- HomeBrew MacOSX Package Manager:
Install:
 /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  

- Ansible: 
  version 2.3.1.0
  python version = 2.7.13 (default, Dec 18 2016, 07:03:39) [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]
  
  
 - Ansible Inventory: 
 
    cp file hosts
    
    [local]
    localhost ansible_connection=local

    [webservers]
    192.168.1.22 ansible_user=root

    [gateway]
    192.168.1.1  ansible_connection=local
  
  - nmap:
  
  
  
    For the sake of brevity we will use 'nmap -F' which scans the top 100 most common ports 
    Use 'nmap -p- ' to scannal all 65535 ports nsise scan.
  
  
  
  
  
 ### Execution of the attack

    Usage:

 - git clone https://github.com/jetweston/SecDevChallenge.git
 - cd SecDevChallenge
 - /usr/local/bin/ansible-playbook portscan.yaml
  
### Postconditions

If the execution was successful, futher to an ansible play variable dump to STDOUT, a log file for each host in /etc/ansible/hoss is saved to /tmp/ in the format {inventory_hostname}_scan.txt:

Sample: 

xanax:SecDevChallenge joseph$ more */private/tmp/localhost_scan.txt*

Nmap 7.70 scan initiated Sat Jul 21 16:27:01 2018 as: nmap -F -oN /tmp/localhost_scan.txt localhost
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00046s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 95 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
443/tcp  open  https
631/tcp  open  ipp
5900/tcp open  vnc

 
