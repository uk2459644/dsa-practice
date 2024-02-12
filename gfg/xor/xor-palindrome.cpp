/**
 * Given an integer n, you need to find the largest integer m(m<n)
 * such that m XOR n is a palindrome. If there is no such integer,
 * return -1.
 * 
*/

/**
 * Approach:
 * 
 * Finding the number of bits in the input integer n using the formula
 * numBits=log2(n)+1 
 * 
 * It then iterates from the maximum possible value of m down to 0.
 * 
 * Inside the loop, the function computes the xor of m and n and checks
 * if it is a palindrome. To check if the XOR is a palindrome, it starts
 * by comparing the first and last bits of the XOR and then moves toward
 * the middle of the XOR, comparing the corresponding bits at each end.
 * 
 * The loop stops as soon as the comparison reaches the middle of the XOR.
 * if the XOR is a palindrome, the function returns m.
 * 
 * If no integer m is found such that m XOR n is a palindrome, the function
 * returns -1.
 * 
 * 
*/

// C++ code for the above approach

// function to find largest integer forming palindrome with n
int largestPalindromeXOR(int n){
    // Find the number of bits in n
    int numBits = log2(n)+1;
    // Iterate from the maximum possible value of m dowm to 0 
    for (int m=n-1;m>=0;m--){
        // compute the XOR of m and n
        int x=m^n;
        // check if the XOR of m and n is a palindrome 
        int i=0, j=numBits-1;
        
    }
}

