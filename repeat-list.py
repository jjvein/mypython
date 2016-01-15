#!/usr/bin/env python

myList = [1,2,3,4,6,7,9,9,12,13,16,16,19,19]
print "Before Sort" , myList
myList.sort()
last = myList[-1]
for i in range(len(myList)-2, -1, -1):
    if last==myList[i]: 
        del myList[i]
    else:
        last = myList[i]

print "After sort:" , myList

