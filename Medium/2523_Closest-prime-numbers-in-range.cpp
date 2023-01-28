/*
Given two positive integers left and right, find the two integers num1 and num2 such that:
    left <= nums1 < nums2 <= right .
    nums1 and nums2 are both prime numbers.
    nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, 
return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.
A number greater than 1 is called prime if it is only divisible by 1 and itself.

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Input: left = 4, right = 6
Output: [-1,-1]
*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        // using Sieve of Eratosthenes method to get primes
        bool prime[right+1];
        memset(prime, true, sizeof(prime));
        prime[1] = false;
        for (int i = 2; i*i <= right; i++) {
            if (prime[i] == true) {
                for (int j = i*i; j <= right; j += i)   prime[j] = false;
            }
        }
        vector<int> p;
        for (int i = left; i<=right; i++){
            if (prime[i])   p.push_back(i);
        }
        
        int result[2];
        vector<int> r;
        if (p.size() == 0 || p.size() == 1)    memset(result, -1, sizeof(result));
        else{
            int min = p[1] - p[0];
            result[0] = p[0]; result[1] = p[1];
            for (int i = 1; i<p.size() - 1; i++){
                if (p[i+1] - p[i] < min){
                    min = p[i+1] - p[i];
                    result[0] = p[i];
                    result[1] = p[i+1];
                }
            }
        }
        for (int i = 0; i<2; i++)   r.push_back(result[i]);
        return r;
    }
};