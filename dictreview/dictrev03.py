def main():
    vendordict = {'cisco':True, 'juniper':False, 'arista':True,'netgear':True}
    custlist = ['acme','globex corporation', 'soylent green', 'intech', 'umbrella corporation']
    print(vendordict)
    print(dir(dict))
    print(vendordict.keys())
    print(vendordict.values())
    print(vendordict.get('juniper'))
    print(vendordict.pop('netgear'))
    print(vendordict.get('netgear'))
    print(dir(list))
    custlist.append('cyberdyne')
    print(custlist)
main()
