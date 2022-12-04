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
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters only.

    Input: s = "Hello World"
    Output: 5

    Input: s = "   fly me   to   the moon  "
    Output: 4

    Input: s = "luffy is still joyboy"
    Output: 6
*/

int lengthOfLastWord(string s) {
    int len = 0;
    int result = 0;
    for (int i = 0; s[i] != '\0'; i++){
        char c = s[i];
        if (c == ' '){
            if (len != 0)   {
                result = len;
            }
            len = 0;
            continue;
        }
        len++;
    }
    result = (len == 0) ? result : len;
    return result;
}

int main(void){
    string s = "luffy is still joyboy";
    cout << lengthOfLastWord(s);
}