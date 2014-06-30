#!/usr/bin/env python
import os

reqs = [] #['example', 'requests']
for req in reqs:
    command = "sudo pip install " + req
    print(command)
    os.system(command)

