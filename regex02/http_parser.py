#!/usr/bin/env python3
import urllib.request
import re

quitcommand = ""
while quitcommand != "q":
    url = input("Where should we search (url)?  ")
    print("Great! So we'll try to open this url " + url + " to search for the phrase:")
    searchFor = input()
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")
    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("No match!")
    quitcommand = input("Press q and hit enter to quit. Anything else to continue")
