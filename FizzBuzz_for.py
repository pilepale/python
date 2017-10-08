# -*- coding: utf-8 -*-

while True:
    broj = int(raw_input("Unesi cijeli broj od 0 do 100: "))
    if broj<0:
        print("Popravite unesenu vrijednost")
    elif broj>100:
        print("Popravite unesenu vrijednost")
    else:
        for i in range(1, broj+1):
            if i % 3 == 0 and i % 5 == 0:
                print "fizzbuzz"
            elif i % 3 == 0:
                print "fizz"
            elif i % 5 == 0:
                print "buzz"
            else:
                print i
        jos = raw_input("Želite li još (Y/N): ")
        jos = jos.upper()
        if jos != "Y":
            print("Hvala na igri, dođite opet :)")
            break