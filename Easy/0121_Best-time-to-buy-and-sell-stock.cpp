/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
*/
#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int m = 0;
        vector <int> profit;
        for (auto i = 0; i < prices.size() - 1; i++){
            for (auto j = i+1; j<prices.size(); j++){
                if (prices[j] - prices[i] > m){
                    m = prices[j] - prices[i];
                    profit.push_back(m);
                }
            }
        }

        if (profit.size() == 0) return 0;
        int max = *max_element(profit.begin(), profit.end());
        return max;
    }
};