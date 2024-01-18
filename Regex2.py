
'''

Hello network!

I decided to write this article as a form of contribution of the network developers community.

Introduction
This article describes how we can filter any IP address in any text or more precisely.

Requirements
-Basic knowledge of networking.
-Medium knowledge of Python programming league.
-Knowledge of regular expressions.

Why this article?
I was working on a project in which I had to develop a DHCP monitoring application using Python.
In the process I had to make a series of filters to discriminate a large number of IP addresses
in different outputs of the network and servers equipment involved. So that wrote this article 
to show how I made the filter.

NOTE: The configuration used on the example is not a real one. I took the structure 
of the "show ip interface brief" command output has a representation. 

'''

#Here is an example script:

import re

pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

data = '''
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0        10.5.5.5         YES NVRAM  up                    up
GigabitEthernet0/1        172.17.0.1       YES NVRAM  up                    up
GigabitEthernet0/3        172.16.5.2       YES NVRAM  up                    up
GigabitEthernet0/4        172.16.100.1     YES NVRAM  up                    up
GigabitEthernet0/5        192.168.1.1      YES NVRAM  up                    up

'''

ips = re.findall(pattern, data)

print(ips)

'''
Explanation


\b =

\\w =

\\W =

(?:A) =

\\d =

{m,n} =

{m} =

'''

'''
Reference:
https://docs.python.org/3/library/re.html

'''