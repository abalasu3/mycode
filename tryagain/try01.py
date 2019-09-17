#!/usr/bin/python3

# Start with an infinite loop
while True:
    try:
        print('Enter a file name: ')
        name = input()
        myfile = open(name, 'w')
        myfile.close()
        break
    except:
        print('Error with that file name! Try again...')
