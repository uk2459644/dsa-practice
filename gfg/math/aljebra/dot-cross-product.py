"""
Dot and cross product of two number.
"""
n=3

def dotProduct(vectA, vectB):
    product=0

    for i in range(n):
        product+=(vectA[i]*vectB[i])
    
    return product

def crossProduct(vectA:list,vectB:list,crossP:list):
    crossP.append(vectA[1]*vectB[2]-vectA[2]*vectB[1])
    crossP.append(vectA[2]*vectB[0]-vectA[0]*vectB[2])
    crossP.append(vectA[0]*vectB[1]-vectA[1]*vectB[0])

    
