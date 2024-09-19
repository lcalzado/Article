# IP filter with python

**Introduction**
This article explains how to filter any IP address from any text or, more precisely, from any output string.

**Requirements**
•	Knowledge of networking.
•	Knowledge of Python programming and regular expressions.

**Why this article?**
I decided to write this article as a way to contribute to the network development community.
I was working on a project where I had to develop a DHCP monitoring application using Python. 
In the process, I needed to create a series of filters to extract a large number of IP addresses 
from different outputs of network equipment and servers. Here's how I achieved that using a simple 
regular expression.

**Note:** The configuration used in the example is not real. I used the structure of the "show ip interface brief" command output as a representation.

Example Script:

```
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
```

Output:

```
['10.5.5.5', '172.17.0.1', '172.16.5.2', '172.16.100.1', '192.168.1.1']
```
**Code Explanation:**
1.	First, I imported the re module.
2.	I created a variable named pattern that contains the regular expression.
3.	Then, I stored the router's output in a variable named data.
4.	The line ips = re.findall(pattern, data) uses the findall function with pattern and data as arguments to find all 
occurrences that match the expression in the data and return them as a Python list.

As we can see from the output, it returned a Python list of strings with all the IP addresses that were shown in the example. 
If you want to learn more about the construction of the regular expression, I have included a link to the official Python documentation 
below so you can analyze it in more detail.

I hope this has been informative for you, and I'd like to thank you for reading it.

**Reference:** https://docs.python.org/3/library/re.html
