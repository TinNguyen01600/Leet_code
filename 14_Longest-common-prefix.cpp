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
    int count = 0;
    int flag = 1;
    int len = strs.size();
    string result = "";
    if (len != 0){
        while(flag == 1){
            char c = strs[0][count];
            for (int i = 1; i<len; i++){
                if (c != strs[i][count]){
                    flag = 0;
                    break;
                }
            }
            if (flag == 0)  continue;
            result.push_back(c);
            count++;
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