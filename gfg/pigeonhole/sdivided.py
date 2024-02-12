"""
Given two integers S and D, the task is to check if the integer S can 
be made divisible by D or not by repeatedly adding S modulo D to S.
if S is divisible by D, then print "Yes". Otherwise print No
"""

"""
Approach: 

The given problem can be solved by using Pigeon Hole Principle.

- According to the principle, if there are more than D numbers that are
  taken modulo with D, then at least one value in the range ([0,D-1]) will
  occur twice. 

- Iterate for (D+1) times and store the value of V(i) in a HashMap, and if 
  there is a repetition then break out of the loop. 

- There is an edge case when the remainder value is 0, exit out of the loop
  in that case as well as this is a case of divisibility, but our logic treats
  it as a cycle.
"""
# Function to check if S is divisible by D while changing S to (S+S%D)

def isDivisibleByDivisor(S,D):
    S%=D 
    # stores the encountered values 
    hashMap=set()
    hashMap.add(S)

    for i in range(D+1):
        S+=(S%D)
        S%=D 
        # check if the value has already been encountered 
        if (S in hashMap):
            # Edge case 
            if (S==0):
                return "Yes"
            return "No"
        # otherwise, insert it into the hashmap 
        else:
            hashMap.add(S)
    
    return "Yes"

