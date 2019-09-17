#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=17042&date=2019-01-21&distance=100&API_KEY=C6B25009-C3CD-4811-97F9-1C1765B1A5A7"#Replace me with AirNows Generated URL

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    ## set up screen
    print("Weather Forecast")
    print("----------------")

    # display the JSON we were returned as Pythonic datastructures
# loop across the list returned to us
    for x in r.json():

        print(x.get("ActionDay"))
        if x.get("ActionDay") == "True":
            print("Its an Action Day. Stay Indoors")
        else:
            print("Its not an Action Day. Go out and have fun")
main()
