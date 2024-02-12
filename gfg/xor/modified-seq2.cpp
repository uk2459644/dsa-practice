/**
 * Efficient Approach:
 * 
 * XOR of A and B produces a set bit when both bits are different
 * and produce an unset bit when both bits are the same. A number can be even
 * only if its LSB is unset. In binary representation, only the LSB
 * contribute to the odd number addition as all other numbers are multiple of 2
 * \addindexthus if the value of X is odd then odd numbers in A will
 * produce even numbers and similarly, if the value of X is even
 * then the even numbers will produce an even value in the new sequence.
 * 
*/

using namespace std;

int findEven(vector<int> A, int N){
    int evenCount=0;

    for (int i:A){
        // Bitwise and with 1 if zero
        // then number is even
        if (!(i&1)){
            evenCount++
        }
    }

    return evenCount;
}

