#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long
/*
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again 
    by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that 
    tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list,
    where the tail connects to the 1st node (0-indexed).

    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, 
    where the tail connects to the 0th node.

    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.
*/


//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> s;
        while (head != NULL){
            if (s.find(head) != s.end())   return true;
            s.insert(head);
            head = head->next;
        }
        return false;
    }
};