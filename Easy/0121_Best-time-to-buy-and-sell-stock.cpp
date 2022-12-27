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
        vector<int> descend = {prices.begin(), prices.end()};
        sort(descend.begin(), descend.end(), greater<int>());
        if (prices == descend)  return 0;

        int max_pos = 0, min_pos = 0;
        int max = prices[0], min = prices[0];
        for (int i = 1; i<prices.size(); i++){
            if (prices[i] > max){  
                max_pos = i;
                max = prices[i];
            }
            if (prices[i] < min){
                min_pos = i;
                min = prices[i];
            }
        }

        if (min_pos < max_pos)  return max - min;
        else{
            vector <int> prices1 = {prices.begin(), prices.begin() + max_pos + 1};
            vector <int> prices2 = {prices.begin() + min_pos, prices.end()};
            int max1 = maxProfit(prices1);
            int max2 = maxProfit(prices2);
            max = (max1 > max2) ? max1 : max2;

            if (max_pos < min_pos - 1){
                vector<int> prices3 = {prices.begin() + max_pos + 1, prices.begin() + min_pos};
                int max3 = maxProfit(prices3);
                if (max3 > max) return max3;
            }
            return max;
        }
    }
};