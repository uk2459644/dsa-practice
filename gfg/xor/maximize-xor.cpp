/**
 * Given a string s consisting of digits and an integer K, the task
 * is to remove exactly K digits from the string so that the remaining
 * digits XOR is maximum.
 * 
*/

/**
 * Approach: 
 * The key insight behind this approach is that we can use the priority
 * queue to keep track of the best XOR values for all possible combinations
 * of the remaining digits, and we can efficiently update the priority
 * queue using the binary representation of the mask.
 * 
 * This allows us to narrow down the search space and find the maximum 
 * XOR value with much less computational effort.
 * 
 * 
*/

#include <bits/std++.h>

using namespace std;

// Function to get maximum xor value
int solve(string s, int k){
    int N=s.length();

    //Initialise queue
    priority_queue<pair<int,int>> pq;

    pq.push({0,0});

    for (int i=0; i<N; i++){
        int digit=s[i]-'0'
        int sz=pq.size();

        for (int j=0; j<sz; j++){
            auto p = pq.top();
            pq.pop();

            int mask=p.first;
            int xor_val=p.second;

            // count set bits 
            int set_bits=__has_builtin_popcount(mask);

            if (set_bits < k){
                pq.push({mask & ~(1<<set_bits), xor_val^digit});
            }

            pq.push({mask & ~(0<<set_bits), xor_val})
            
        }
    }
}