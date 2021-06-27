#!/usr/bin/env python3

import requests
import random
import json

class Scam:
    def __init__(self):
        self.names = json.loads(open("names.json").read())
        print("loading passwords...")
        self.passwords = json.loads(open("/opt/rockyou.json").read())
        print("passwords loaded")

    def Generate_Email(self) -> str:
        # Generate an email to be used in the request

        name = (''.join(random.choice(self.names)))
        name2 = (''.join(random.choice(self.names)))

        email = ("%s.%s@gmail.com" % (name.lower(), name2.lower()))
        return email

    def Generate_Password(self) -> str:
        # Use a password from rockyou in the request

        password = (''.join(random.choice(self.passwords)))
        return password

    def Send_Request(self, url) -> bool:
        # This is the part of the class that actually sends the request to the scam server.

        email = self.Generate_Email()
        password = self.Generate_Password()
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

        r = requests.post(url, allow_redirects=False, headers=header, data={
            "username": email,
            "password": password
        })

        if r:
            print(f"SENT [{email}:{password}]:[{r}]")
            return True
        else:
            print(f"SENT [{email}:{password}]:[{r}]")
            return False

        """
		outputs the username, password sent to the server
		also outputs the status given by the server
		if the response code is not 200, it returns false
		ex: [<Response [405]>]
		"""

scam = Scam()
