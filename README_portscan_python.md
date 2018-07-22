# SecDevChallenge
______
## Solutions 1. Ansible and Python
______
## Introduction

#### Background

### Exploit T1046: Network Service Scanning & Discovery

"Network Service Scanning:      Discovery:      T1046   Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulneraÂble
to remote software exploitation. Methods to acquire this information
include port scans and vulnerability scans using tools that are brought onto a system " - reference: https://attack.mitre.org/wiki/Main_Page

Network service port scanning range from "well-known" UDP/TCP ports (0 to 1023 ),
"registered ports" (1024 to 49151), to "public" ports (49152 to 65535).


## Objective

The Object of this challenge is __automate attack technique T1046__.

### Solution

In line with the objectives of the challenge I have chosen to deliver a solution based on a combination of __Ansible__ and __Python__ script , running  on a CentOS (Linux) Operating System, to achieve the goal.

__note__: Scanning 65353 port will take considerable time and compute. For the sake of brevity the solution described herein will  be limited to the set of the top-100 well known ports.


### Pre-conditions:


- __Operating System__: CentOS Linux7.4.1708

```
version info:

[joseph@effexor SecDevChallenge]$ more /etc/redhat-release
CentOS Linux release 7.4.1708 (Core)
Linux 3.10.0-693.11.1.el7.x86_64 #1 SMP Mon Dec 4 23:52:40 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```


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

   -  cp __/tmp/SecDevChallenge/hosts__ __/etc/ansible/hosts__

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

2.  git clone https://github.com/jetweston/SecDevChallenge.git

```
 [joseph@effexor tmp]$ git clone https://github.com/jetweston/SecDevChallenge.git
 Cloning into 'SecDevChallenge'...
 remote: Counting objects: 91, done.
 remote: Compressing objects: 100% (81/81), done.
 remote: Total 91 (delta 37), reused 4 (delta 2), pack-reused 0
 Unpacking objects: 100% (91/91), done.
 ```

 3. cd SecDevChallenge


 4. [SecDevChallenge]$ __ansible-playbook portscan_python.yaml__

```
[joseph@effexor SecDevChallenge]$ ansible-playbook portscan_python.yaml

PLAY [all] ********************************************************************************************************************

TASK [install required packages] **********************************************************************************************
ok: [localhost] => (item=[u'nmap', u'python'])

TASK [install the Pythson package, force upgrade] *****************************************************************************
ok: [localhost] => (item=pip)

TASK [set_fact] ***************************************************************************************************************
ok: [localhost]

TASK [debug] ******************************************************************************************************************
ok: [localhost] => {
    "date": "20180722164732"
}

TASK [Run NMAP using Anisible commnd module] **********************************************************************************
changed: [localhost]

TASK [debug] ******************************************************************************************************************
ok: [localhost] => {
    "output": {
        "changed": true,
        "cmd": [
            "/usr/local/bin/python3",
            "/tmp/SecDevChallenge/portscan.py",
            "localhost"
        ],
        "delta": "0:00:01.427605",
        "end": "2018-07-22 16:47:34.315557",
        "failed": false,
        "rc": 0,
        "start": "2018-07-22 16:47:32.887952",
        "stderr": "",
        "stderr_lines": [],
        "stdout": "\u001b[3;J\u001b[H\u001b[2J------------------------------------------------------------\nPlease wait, scanning remote host 127.0.0.1\n------------------------------------------------------------\nPort 22:  Open\nPort 25:  Open\nPort 80:  Open\nPort 88:  Open\nPort 111:  Open\nPort 389:  Open\nPort 464:  Open\nPort 631:  Open\nPort 749:  Open\nPort 3306:  Open\nPort 10000:  Open\nPort 34274:  Open\nScanning Completed",
        "stdout_lines": [
            "\u001b[3;J\u001b[H\u001b[2J------------------------------------------------------------",
            "Please wait, scanning remote host 127.0.0.1",
            "------------------------------------------------------------",
            "Port 22:  Open",
            "Port 25:  Open",
            "Port 80:  Open",
            "Port 88:  Open",
            "Port 111:  Open",
            "Port 389:  Open",
            "Port 464:  Open",
            "Port 631:  Open",
            "Port 749:  Open",
            "Port 3306:  Open",
            "Port 10000:  Open",
            "Port 34274:  Open",
            "Scanning Completed"
        ]
    }
}

PLAY RECAP ********************************************************************************************************************
localhost                  : ok=6    changed=1    unreachable=0    failed=0   

```


## Postconditions

None.
