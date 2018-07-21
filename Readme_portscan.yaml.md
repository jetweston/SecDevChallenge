---
- hosts: local
  gather_facts: False
  tasks:
    - name: Run NMAP using Anisible commnd module
      command: nmap -F -oN /tmp/{{inventory_hostname}}_scan.txt {{inventory_hostname}}
      register: output
    - debug:
        var: output