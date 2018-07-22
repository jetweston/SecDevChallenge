## SecDevChallenge

### Exploit T1046: Network Service Scanning & Discovery 

Network Service Scanning:	Discovery:	T1046	Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information include port scans and vulnerability scans using tools that are brought onto a system (reference: https://attack.mitre.org/wiki/Main_Page)

Port TCP Rages:
Ports 0 to 1023 are Well-Known Ports.
Ports 1024 to 49151 are Registered Ports (often registered by a software developer to designate a particular port for their application)
Ports 49152 to 65535 are Public Ports.

### Pre-conditions:


- Linux 3.10.0-693.11.1.el7.x86_64 #1 SMP Mon Dec 4 23:52:40 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

 - install nmap package: 
    - yum install nmap
 
  

- Ansible: 

  ansible 2.4.2.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/joseph/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.5 (default, Aug  4 2017, 00:39:18) [GCC 4.8.5 20150623 (Red Hat 4.8.5-16)]
  
 - Ansible Inventory: 
  
   /etc/ansivle/hosts
   
  
   [local]
   localhost ansible_connection=local

   [webservers]
   192.168.1.22 ansible_user=root

   [gateway]
   192.168.1.1  ansible_connection=local
  
 - Nmap:
 
  Nmap version 6.40 ( http://nmap.org )
  Platform: x86_64-redhat-linux-gnu
  Compiled with: nmap-liblua-5.2.2 openssl-1.0.2k libpcre-8.32 libpcap-1.5.3 nmap-libdnet-1.12 ipv6

 For the sake of brevity we will use 'nmap -F' which scans the top 100 most common ports 
 Use 'nmap -p- ' to scannal all 65535 ports nsise scan.
 
  
 ### Execution of the attack

    Usage:

 - git clone https://github.com/jetweston/SecDevChallenge.git
 - cd SecDevChallenge
 - /usr/local/bin/ansible-playbook portscan.yaml
  
### Postconditions

If the execution was successful, futher to an ansible play variable dump to STDOUT, a log file for each host in /etc/ansible/hoss is saved to /tmp/ in the format {inventory_hostname}_scan.txt:


[joseph@effexor SecDevChallenge]$ ls -la

# Nmap 6.40 scan initiated Sun Jul 22 06:10:38 2018 as: nmap -F -oN /tmp/localhost_scan.txt localhost
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00031s latency).
Other addresses for localhost (not scanned): 127.0.0.1
Not shown: 91 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
25/tcp    open  smtp
80/tcp    open  http
88/tcp    open  kerberos-sec
111/tcp   open  rpcbind
389/tcp   open  ldap
631/tcp   open  ipp
3306/tcp  open  mysql
10000/tcp open  snet-sensor-mgmt


# Nmap done at Sun Jul 22 06:10:38 2018 -- 1 IP address (1 host up) scanned in 0.03 seconds

 
