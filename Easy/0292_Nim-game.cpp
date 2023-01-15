/*
You are playing the following Nim Game with your friend:
    Initially, there is a heap of stones on the table.
    You and your friend will alternate taking turns, and you go first.
    On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
    The one who removes the last stone is the winner.
Given n, the number of stones in the heap, 
return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

Input: n = 4
Output: false

Input: n = 1
Output: true

Input: n = 2
Output: true
*/

/*
It can easily be seen that if n % 4 != 0 I always wins
for ex:  
    n=5: me(1) -> friend(1/2/3) -> me(3/2/1)(last stone)
        no matter how many stones friend picks in his turn, there is always x stones left (1 <= x <= 3) for me to pick
        in my last turn
    n=6: me(2) -> friend(1/2/3) -> me(3/2/1)(last stone)
    n=7: me(3) -> friend(1/2/3) -> me(3/2/1)(last stone)
*/

#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

class Solution {
public:
    bool canWinNim(int n) {
        if (n % 4 == 0) return false;
        return true;
    }
};