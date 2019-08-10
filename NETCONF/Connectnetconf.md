#Exploring NETCONF

This project demonstrates how to use an SSH client that creates 
and interactive NETCONF session on Cisco IOS-XE

Connect to the Cisco IOS-XE router via ssh on Port 830

$ ssh -p 830 ntc@ios-csr1kv

After conncetion, the NETCONF server (Cisco IOS-XE router) 
responds with an hello message that includes all it's supported NETCONF 
Capabilities including NETCONF Operations,capabilities,models/schema
and a session ID 



