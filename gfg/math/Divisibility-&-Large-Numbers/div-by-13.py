# A number is divisible by 13 if and if the
# alternating sum of blocks of three from right to left
# is divisble by 13

# A number is divisible by 13 if and only if 
# the number obtained by adding the last digit
# multiplied by 4 to the rest is also divisible by 13

def checkDivi(num):
    length = len(num)
    if (length == 1 and num[0]=='0'):
        return True
    # Append required 0s at the beginning
    if (length%3==1):
        num = str(num)+'00'
        length+=2
        
    elif (length % 3 == 2):
         
        # Same as strcat(num, "0");
        # in c.
        num = str(num) + "0"
        length += 1
 
    # Alternatively add/subtract digits 
    # in group of three to result.
    sum = 0
    p = 1
    for i in range(length - 1, -1 , -1) :
         
        # Store group of three
        # numbers in group variable.
        group = 0
        group += ord(num[i]) - ord('0')
        i -= 1
        group += (ord(num[i]) - ord('0')) * 10
        i -= 1
        group += (ord(num[i]) - ord('0')) * 100
 
        sum = sum + group * p
 
        # Generate alternate series
        # of plus and minus
        p *= (-1)
    sum = abs(sum)
    return (sum % 13 == 0)