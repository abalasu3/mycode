#!/usr/bin/env python3
us_invasion = [{'ip':'10.10.1.2', 'un':'john', 'pw':'allstar'},{'ip':'10.10.1.3', 'un':'paul', 'pw':'iils20s3'}, {'ip':'10.10.1.4', 'un':'george', 'pw':'hunkydoryzory'}, {'ip':'10.10.1.5', 'un':'stuart', 'pw':'alta3'}, {'ip':'10.10.1.6', 'un':'pete', 'pw':'a8dd827z3'}]
def byUserName(x):
    return x['un']
listbyusername = sorted(us_invasion, key=byUserName)
print("\nThe list us_invasion looks like: ", us_invasion)
print("\nResult of sorted(us_invasion, key=byUserName): ", listbyusername)
print("\nResult of sorted(us_invastion, key= lambda x:x['un']): ", sorted(us_invasion, key =lambda x:x['un']))
print("\nResult of sorted(us_invastion, key= lambda x:x['ip']): ", sorted(us_invasion, key =lambda x:x['ip']))
print("\nResult of sorted(us_invastion, key= lambda x:x['pw']): ", sorted(us_invasion, key =lambda x:x['pw']))
print("\nResult of sorted(us_invastion, key= lambda x:x['pw'][-1]): ", sorted(us_invasion, key =lambda x:x['pw'][-1]))
print("\nBut the value of the list us_invasion hasn't actually changed: ", us_invasion)

