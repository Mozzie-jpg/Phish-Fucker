#!/usr/bin/env python3

from scam import *

url = input("url: ")
s = scam.Send_Request(url)
if s:
    while True:
        scam.Send_Request(url)
else:
    quit()
