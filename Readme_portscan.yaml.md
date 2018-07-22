# SecDevChallenge

## Introduction

#### Background

### Exploit T1046: Network Service Scanning & Discovery

"Network Service Scanning:	Discovery:	T1046	Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable
to remote software exploitation. Methods to acquire this information
include port scans and vulnerability scans using tools that are brought onto a system " - reference: https://attack.mitre.org/wiki/Main_Page

Network service port scanning range from "well-known" UDP/TCP ports (0 to 1023 ),
"registered ports" (1024 to 49151), to "public" ports (49152 to 65535).


## Objective

The Object of this challenge is __automate attack technique T1046__.

### Solution

In line with the objectives of the challenge I have chosen to deliver a solution based on a combination of __Ansible__ and __bash__ , running  on a CentOS (Linux) Operating System, to achieve the goal.

__note__: Scanning 65353 port will take considerable time and compute. For the sake of brevity the solution described herein will  be limited to the set of the top-100 well known ports. 


### Pre-conditions:


- __Operating System__: CentOS Linux7.4.1708

```
version info:

[joseph@effexor SecDevChallenge]$ more /etc/redhat-release
CentOS Linux release 7.4.1708 (Core)
Linux 3.10.0-693.11.1.el7.x86_64 #1 SMP Mon Dec 4 23:52:40 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux```


- __Ansible__: (packages install: yum install ansible)


  ```
  version info:

  ansible 2.4.2.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/joseph/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.5 (default, Aug  4 2017, 00:39:18) [GCC 4.8.5 20150623 (Red Hat 4.8.5-16)]

  ```

 - __Ansible Inventory__ (Hosts) file:

   joseph@effexor SecDevChallenge] __/etc/ansible/hosts__

```

   [local]
   localhost ansible_connection=local

   [webservers]

   [switches]

```

note: "ansible_connection=local" tells ansible bypass using SSH run the playbook.

- __NMAP__: (packages install: yum install nmap)

```
version info:

nmap version 6.40 ( http://nmap.org )
Platform: x86_64-redhat-linux-gnu
Compiled with: nmap-liblua-5.2.2 openssl-1.0.2k libpcre-8.32 libpcap-1.5.3 nmap-libdnet-1.12 ipv6
Compiled without:
Available nsock engines: epoll poll select
```

 ### Execution of the attack


1. cd /tmp

2. git clone https://github.com/jetweston/SecDevChallenge.git

```
 [joseph@effexor tmp]$ git clone https://github.com/jetweston/SecDevChallenge.git
 Cloning into 'SecDevChallenge'...
 remote: Counting objects: 91, done.
 remote: Compressing objects: 100% (81/81), done.
 remote: Total 91 (delta 37), reused 4 (delta 2), pack-reused 0
 Unpacking objects: 100% (91/91), done.
 
 ```

 3. cd SecDevChallenge

 4. [SecDevChallenge]$ ansible-playbook portscan.yaml

```
joseph@effexor SecDevChallenge]$ ansible-playbook portscan.yaml

PLAY [all] ********************************************************************************************************************

TASK [Run NMAP using Anisible commnd module] **********************************************************************************
changed: [localhost]

TASK [debug] ******************************************************************************************************************
ok: [localhost] => {
    "output": {
        "changed": true,
        "cmd": [
            "nmap",
            "-F",
            "-oN",
            "/tmp/localhost_scan.txt",
            "localhost"
        ],
        "delta": "0:00:00.054745",
        "end": "2018-07-22 07:07:47.186636",
        "failed": false,
        "rc": 0,
        "start": "2018-07-22 07:07:47.131891",
        "stderr": "",
        "stderr_lines": [],
        "stdout": "\nStarting Nmap 6.40 ( http://nmap.org ) at 2018-07-22 07:07 EDT\nNmap scan report for localhost (127.0.0.1)\nHost is up (0.00068s latency).\nOther addresses for localhost (not scanned): 127.0.0.1\nNot shown: 91 closed ports\nPORT      STATE SERVICE\n22/tcp    open  ssh\n25/tcp    open  smtp\n80/tcp    open  http\n88/tcp    open  kerberos-sec\n111/tcp   open  rpcbind\n389/tcp   open  ldap\n631/tcp   open  ipp\n3306/tcp  open  mysql\n10000/tcp open  snet-sensor-mgmt\n\nNmap done: 1 IP address (1 host up) scanned in 0.04 seconds",
        "stdout_lines": [
            "",
            "Starting Nmap 6.40 ( http://nmap.org ) at 2018-07-22 07:07 EDT",
            "Nmap scan report for localhost (127.0.0.1)",
            "Host is up (0.00068s latency).",
            "Other addresses for localhost (not scanned): 127.0.0.1",
            "Not shown: 91 closed ports",
            "PORT      STATE SERVICE",
            "22/tcp    open  ssh",
            "25/tcp    open  smtp",
            "80/tcp    open  http",
            "88/tcp    open  kerberos-sec",
            "111/tcp   open  rpcbind",
            "389/tcp   open  ldap",
            "631/tcp   open  ipp",
            "3306/tcp  open  mysql",
            "10000/tcp open  snet-sensor-mgmt",
            "",
            "Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds"
        ]
    }
}

PLAY RECAP ********************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0  


```


## Postconditions

### Post-Implementation-Validation (PIV)

1.  Further to an ansible playbook variable dump to STDOUT, for each host defined in /etc/ansible/hosts an scan output will be produced and stored in  /tmp  in the format _{inventory_hostname}_scan.txt__:


localhost_scan.txt
```
[joseph@effexor SecDevChallenge]$ more /tmp/localhost_scan.txt

# Nmap 6.40 scan initiated Sun Jul 22 07:07:47 2018 as: nmap -F -oN /tmp/localhost_scan.txt localhost

Nmap scan report for localhost (127.0.0.1)
Host is up (0.00068s latency).
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

# Nmap done at Sun Jul 22 07:07:47 2018 -- 1 IP address (1 host up) scanned in 0.04 seconds
```
