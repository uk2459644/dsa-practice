# Count number of ways to cover a distance

def printCountRec(dist):
    # base case
    if dist < 0:
        return 0
    
    if dist == 0:
        return 1
    
    # recur for all previous 3 and add the results
    return (printCountRec(dist-1)+printCountRec(dist-2)+printCountRec(dist-3))

