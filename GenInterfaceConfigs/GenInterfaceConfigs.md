#Generating Interface configurations from a List of dictionaries

Using  a Jinja template to iterate over a list of dictionaries containing attributes for each interface
Each Interface has it's own dictionary where the keys are attributes for each network interface 
Attributes include 
1. Name
2. Description
3. or Uplink 

The Jinja Template is to iterate over each to produce configuration as follows 


interface GigabitEthernet0/1
    description Uplink Port
    
        switchport mode trunk 
    
    
interface GigabitEthernet0/2
    description Server port number one
    
    switchport access vlan 10
    switchport mode access

    
    
interface GigabitEthernet0/3
    description Server port number two
    
    switchport access vlan 10
    switchport mode access




