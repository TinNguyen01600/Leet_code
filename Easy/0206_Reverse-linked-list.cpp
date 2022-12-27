#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

/*
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Input: head = [1,2]
    Output: [2,1]

    Input: head = []
    Output: []
*/

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void push(ListNode** head_ref, int new_data){
        ListNode* new_node = new ListNode();
        new_node->val = new_data;
        new_node->next = (*head_ref);
        (*head_ref) = new_node;
    }
    ListNode* reverseList(ListNode* head) {
        vector <int> s;
        while (head != NULL){
            s.push_back(head -> val);
            head = head -> next;
        }
        ListNode* result = NULL;
        for (int i = 0; i<s.size(); i++){
            push(&result, s[i]);
        }
        return result;
    }
};