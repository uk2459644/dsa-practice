"""
Given two integers A and B, the task is to find a triplet (X,Y,Z)
such that all of them are divisible by A, exactly one of them is divisible
by both A and B, and X+Y=Z

"""
"""
Approach: The given problem is an observation-based problem that can be
solved using basic mathematics. It can be observed that the triplet
(A,A*B,A*(B+1)), satisfies all of the given conditions except when the value
of B is 1. 
"""

def findTriplet(A,B):
    if (B==1):
        print(-1)
        return 
    
    print((A,A*B,(A*(B+1))))
