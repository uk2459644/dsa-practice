
mod=1e9+7

# function which returns the number of ways to decode the message
def decodeMessage(dp,s,str,n):

    # an empty string can also form 1 valid decoding
    if (s>=n):
        return 1
    
    # If we have already computed the number of ways to decode the
    # substring return the answer directly
    if (dp[s]!=-1):
        return dp[s]
    
    num=0
    tc=0

    for i in range(s,n):
        # generate the number 
        num=num*10+(ord(str[i]))-ord('0')
        # validate the number
        if num>=1 and num<= 26:
            # since the number of ways to decode any string depends on the
            # result of how the remaining string is decoded so get the
            # number of ways how the rest of the string can be decoded
            c=decodeMessage(dp,i+1,str,n)
            # and all the ways that the substring from the current index can
            # be decoded
            tc=int((tc%mod+c%mod)%mod)
        else:
            # leading 0s or the number generated so far is greater than 26
            # we can just stop the process as it can never be a part of our
            # solution
            break

        dp[s]=tc

        return dp[s]
    



