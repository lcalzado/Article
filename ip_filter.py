'''
Hello network!

Introduction
This article describes how we can filter any IP address in any text or more precisely any output string.

Requirements
-knowledge of networking.
-knowledge of Python programming league and regular expression.

Why this article?
I decided to write this article as a form of contribute the network developers community.

I was working on a project in which I had to develop a DHCP monitoring application using Python.
In the process I had to make a series of filters to discriminate a large number of IP addresses
in different outputs of the network equipments and servers involved. And here is how I made it
just using a simple regular expresion.

NOTE: The configuration used on the example is not a real one. I took the structure 
of the "show ip interface brief" command output as a representation. 

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
output:
['10.5.5.5', '172.17.0.1', '172.16.5.2', '172.16.100.1', '192.168.1.1']

'''

'''
Code Explanation:

1. First I imported the re module.
2. Created a variable named "pattern" that contain the regular expression.
3. Then I storaged the router's output in a variable named data. 
4. The line "ips = re.findall(pattern, data)" uses the findall function with the "pattern" and "data" as arguments to parse all the recurrences that matches 
the expression in the data and return a python list of them. 

As we can see in the output, it returned python list of strings with all the ip addresses that were shown in the example. If you want to know more about the construccion 
of the regular expression I leave you the below link to the official Python documentation so you can analyze it in more detail.

I hope this has been informative for you and I'd like to thank you for reading it.
'''

'''
Reference:
https://docs.python.org/3/library/re.html

'''
