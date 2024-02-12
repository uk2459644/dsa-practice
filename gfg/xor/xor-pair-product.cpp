/**
 * Given a positive integer value V, the task is 
 * to find the maximum XOR of two numbers such that
 * their product is equal to the given value V.
*/

/**
 * The approach takes advantage of the fact that if a
 * and b are two numbers such that a*b=value, then the xor
 * of a and b will be maximum when a and b are as close to each other 
 * as possible. By iterating through the numbers up to the square root
 * of the given value, we cover all possible pairs of factors and find
 * the maximum xor among them.
 * 
*/

// C++ code for the above approach
#include <cmath>
#include <iostream>

// find maximum xor pair value
int find_max_xor_product(int value){
    int max_xor = 0;
    // calculate the square root of the given value
    int sqrt_value = sqrt(value);
    // iterate from 1 to the square root of the value 
    for(int num=1; num<=sqrt_value;++num){
        // check if num is a divisor of the value 
        if (value%num==0){
            // Calculate the corresponding divisor
            int div=value/num;
            max_xor = std::max(max_xor,num^div);
        }
    }

    // return the maximum XOR value
    return max_xor;
}

