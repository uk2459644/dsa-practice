/**
 * Given two strings s1 and s2, the task is to find the length of the longest
 * common substring of s1 and s2 such that the XOR is maximum.
 * 
*/

/**
 * Approach : 
 * This approach uses the fact that two binary numbers have the same 
 * XOR value if and only if their bitwise XOR operation is a power of 2.
 * Therefore, we generate all possible substrings of s1 and tore their hash
 * values in a set. Then we generate all possible substrings of s2 and check
 * if their hash value is present in the set, we update the maximum XOR value
 * to the length of the substring.
 * 
*/

// Function to find length of longest common substring whose XOR is maximum

int max_xor_common_substring(
    string s1, string s2
){
    int n1=s1.length(), n2= s2.length();
    int max_xor=0;

    // DEclaring unordered_Set
    unordered_set<int> s; 

    for (int len=1; len<=n1; len++){
        s.clear();
        int hash_val=0;

        // Start Iterating 
        for (int i=0; i<len; i++){
            hash_val = (hash_val<<1)+(s1[i]-'0');
        }
        s.insert(hash_val);

        for(int i=len; i<n1; i++){
            hash_val = ((hash_val<<1)+(s1[i]-'0'))&((1<<len)-1);
            s1.insert(hash_val);
        }
    }
}

