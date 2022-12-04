#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <vector>
#include <conio.h>
#include <list>
#include <unordered_map>
#include <stdlib.h>
#include <set>
#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

/*
    Write a function to find the longest common prefix string amongst an array of strings.

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Input: strs = ["dog","racecar","car"]
    Output: ""
*/

string longestCommonPrefix(vector<string>& strs) {
    int len = strs.size();
    string result = "";
    
    if (len != 0){
        for (int i = 0; i<strs[0].length(); i++){
            char c = strs[0][i];
            for (int j = 1; j<len; j++){
                if (c != strs[j][i])    return result;
            }
            result.push_back(c);
        }
    }
    return result;
}

int main(void){
    vector<string> strs;
    strs.push_back("flower");
    strs.push_back("flow");
    strs.push_back("flight");
    strs.push_back("flex");

    cout << longestCommonPrefix(strs) << endl;
}