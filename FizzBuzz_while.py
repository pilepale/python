# -*- coding: utf-8 -*-

i=1

while True:
    broj = int(raw_input("Unesi cijeli broj od 0 do 100: "))
    if broj<0:
        print("Popravite unesenu vrijednost")
    elif broj>100:
        print("Popravite unesenu vrijednost")
    else:
        while i < broj+1:
            if i % 3 == 0 and i % 5 == 0:
                print "fizzbuzz"
            elif i % 3 == 0:
                print "fizz"
            elif i % 5 == 0:
                print "buzz"
            else:
                print i
            i = i+1
        i=1
        jos = raw_input("Želite li još (Y/N): ")
        jos = jos.upper()
        if jos != "Y":
            print("Hvala na igri, dođite opet :)")
            break



