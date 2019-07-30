# NetworkAutomation --  Switch port configuration

Project elaborates two ways of writing data into a jinja template to configure a basic switchport configuration
1.Python dictionary
2. Python Class.

The Python script renders a Jinja Template file with the configuration files </br>
In the python Script is a  dictionary where the template variables get data from

Script defines the template variables in the Jinja template using a dictionary and writes into the jinja template </br>

with final output like? which is also the same had one used a Python class</br>

interface GigabitEthernet0/1 </br>
description Server Port  </br>
switchport access vlan 10 </br>
switchport mode access
