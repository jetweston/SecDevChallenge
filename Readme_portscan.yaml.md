---
- hosts: local
  gather_facts: False
  tasks:
    - name: Run NMAP using Anisible commnd module
      command: nmap -p- -oN /tmp/{{inventory_hostname}}_scan.txt {{inventory_hostname}}
      register: output
    - debug:
        var: output
