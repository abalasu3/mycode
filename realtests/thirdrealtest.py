#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = "https://swapi.co/api/people/1/?format=json"

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    print("Name -" + requests.get(LOOKUPAPI).json().get("name") + ";Hair Color - " + requests.get(LOOKUPAPI).json().get("hair_color")) 

    # display the JSON we were returned as Pythonic datastructures
    #force_json = r.json()

    #print("Name - " + force_json.get("name")) 
    #print("Hair Color - " + force_json.get("hair_color"))
    
main()
