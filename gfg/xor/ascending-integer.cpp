/**
 * 
 * Given three distinct integers X,Y,Z Find an integer N that after
 * performing XOR of each element, integer must follow that X should
 * be minimum and Z should be maximum between three integers. If possible then
 * the integer, Otherwise print -1.
 * 
*/

/**
 * The approach checks if the three integers are sorted in ascending
 * or descending order. If it is sorted in ascending order, it outputs 0,
 * because we know that Any number XOR 0 = That Number. If it is sorted
 * in descending order, calculates the next positive integer of the maximum
 * inteer which is a power of 2, and prints that number -1.
 * If the array is not sorted, it outputs -1.
 * 
*/

#include <bits/std++.h>
using namespace std;

void sortThreeInteger(int X, int Y, int Z, int n){

    // Check if the three integers sorted in ascending order
    if (X<Y && Y<Z){
        // If they sorted in ascending order, output "Yes 0"
        cout << 0 << endl ;
    }

    // Check if the three integers are sorted in descending order
    else if (X>Y && Y>Z)
    {
        /* code */
        // If three integers are sorted in descending order, compute the smallest
        // power of 2 greater than the first element minus one

        // Compute the logarithm of the first element to base 2
        int d=log2(X)

        // Compute the smallest power of 2 greater than the logarithm
        int u=pow(2,d+1);

        // Output "Yes" followed by the computed value
        cout << u-1 << endl ;


    }
    // If the integers are not sorted, output "No"
    else {
        cout << -1 << endl ;
    }

}


