def main():
    firewalldict = {'sip':'5060', 'ssh':'22', 'http':'80'}
    print(firewalldict)
    firewalldict['https'] = 443
    print(firewalldict)
    print('The print statement can be passed multiple times, provided they are separated by commas')
    print("The port in use for HTTP Secure is:",firewalldict['https'])
    print("A safer way to recall that data is to use the .get method:", firewalldict.get('razzledazzlerootbeer'))
    print(firewalldict.keys())
    print(firewalldict.values())

main()
