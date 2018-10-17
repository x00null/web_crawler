#!/usr/bin/env python

import requests

def request(url):

    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass

target_url = "www.multiconsult.com.ni"

with open("/Users/Harcrack/files_dirs.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print ("Discovered Pages -->" + test_url)

