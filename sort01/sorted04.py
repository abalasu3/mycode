#!/usr/bin/env python3
simpsons = [ ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]
def byAge(x):
    return x[1]
def secondletter(x):
    return x[0][1]
simpsonsAge = sorted(simpsons, key=byAge)
secondsimpsons = sorted(simpsons, key = secondletter)
print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)
print('Result of sorted(simpsons, key=secondletter): ', secondsimpsons)

