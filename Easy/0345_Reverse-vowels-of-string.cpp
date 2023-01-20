/*
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"

Input: s = "aA"
Output: "Aa"
*/

#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    string reverseVowels(string s) {
        vector<char> vowels{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        vector<char> s_vowels, s_consonant;
        for (int i = 0; i<s.size(); i++){
            if (find(vowels.begin(), vowels.end(), s[i]) != vowels.end()){
                s_vowels.push_back(s[i]);
            }
        }

        string result;
        int count_vowel = 0;
        for (int i = 0; i<s.size(); i++){
            if (find(vowels.begin(), vowels.end(), s[i]) != vowels.end()){
                result += s_vowels[s_vowels.size() - 1 - count_vowel];
                count_vowel++;
            }
            else    result += s[i];
        }
        return result;
    }
};