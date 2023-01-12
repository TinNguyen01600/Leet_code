/*
We define the usage of capitals in a word to be right when one of the following cases holds:
    - All letters in this word are capitals, like "USA".
    - All letters in this word are not capitals, like "leetcode".
    - Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Input: word = "USA"
Output: true

Input: word = "FlaG"
Output: false
*/

#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    bool detectCapitalUse(string word) {
        vector<int> pos;
        for (int i = 0; i<word.size(); i++){
            if (int(word[i]) >= 65 && int(word[i]) <= 90){
                cout << word[i];
                pos.push_back(i);
            }
        }
        
        if (pos.size() == 0 || pos.size() == word.size()) return true;
        if (pos.size() == 1 && pos[0] == 0) return true;
        return false;
    }
};