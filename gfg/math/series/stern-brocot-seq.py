
import math 

def SternSequenceFunc(BrocotSequence,n):
    for i in range(1,n):
        considered_element = BrocotSequence[i]
        precedent = BrocotSequence[i-1]

        # adding sum of condiered elementand
        # it's precendent
        BrocotSequence.append(considered_element+precedent)

        # adding next considered element
        BrocotSequence.append(considered_element)

        for i in range(0,15):
            print(BrocotSequence[i], end=" ")
    
n=15 
BrocotSequence = []

BrocotSequence.append(1)
BrocotSequence.append(1)
SternSequenceFunc(BrocotSequence,n)
