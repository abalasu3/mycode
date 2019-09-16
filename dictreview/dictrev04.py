def main():
    vendordict ={'cisco':True, 'juniper':False, 'arista': True, 'netgear':True}
    custlist = ['acme','globex corporation', 'soylent green', 'intiech', 'umbrella corporation']
    print(dir(dict))
    print(dir(list))
    #print(custlist.keys())
    print(vendordict.get('juniper'))
    #print(custlist.get('umbrella corporation'))
    #custlist.update('nsx')
    vendordict.update({'cisco':False})
    #vendordict.sort()
main()
