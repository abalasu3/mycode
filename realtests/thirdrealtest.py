#!/usr/bin/env python3
# imports always go at the top of your code
import requests
import argparse

LOOKUPAPI = "https://swapi.co/api/people/1/?format=json"

def main():

    parser = argparse.ArgumentParser(description='Add a gender attribute')
    parser.add_argument('-attr', metavar='attribute', type=str,
                        help='Ask for any attriute')
    parser.add_argument('-k', '--keyz', help='Returns list of attribute keys to be passed to "-attr"', action="store_true")
    args = parser.parse_args()
    force_json = requests.get(LOOKUPAPI).json()
    keys =  list(force_json.keys())
    if args.attr == "homeworld":
        planet_json = requests.get(force_json.get(args.attr)+"?format=json").json()
        print(f'Name - {force_json.get("name")}\nHair Color - {force_json.get("hair_color")}\nOptional Attribute:{args.attr} - {planet_json.get("name")}')
    else:
        print(f'Name - {force_json.get("name")}\nHair Color - {force_json.get("hair_color")}\nOptional Attribute:{args.attr} - {force_json.get(args.attr)}') 
    print("------------------------------------------------------------------------------------------------------------------------")
    if args.keyz:
        print("Try running the script again.This time choose any attribute from the list and pass them as argument with -attr")
        for key in keys:
            print(key)
main()
