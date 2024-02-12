/**
 * Given a range, find the XOR of the smallest and largest triangular numbers
 * within that range.
 * 
*/

/**
 * A triangular number is a number that can be represented as the sum of consecutive
 * positive integers starting from 1. In other words, a triangular number
 * is the sum of the first n natural numbers, where n is a positive number is:
 * Tn=n(n+1)/2 
 * 
 * 
*/

/**
 * Approach: 
 * 
 * The idea behind this approach is to first define a function to find the
 * nth triangular number using the formula n*(n+1)/2. Then, we define two functions
 * to find the smallest and largest triangular number within a given range.
 * 
*/

// C++ code of the above approach 

// function to find triangular number 
int findTriangularNumber(int n){
    return n*(n+1)/2 ;
}

// Function to find smallest triangular number above the smallest range
int findSmallestTriangularNumber(int lowerBound, int upperBound){
    
}
