#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

/*
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together 
    the nodes of the first two lists.
    Return the head of the merged linked list.

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Input: list1 = [], list2 = []
    Output: []

    Input: list1 = [], list2 = [0]
    Output: [0]
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

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        vector <int> s;
        while (list1 != NULL){
            s.push_back(list1 -> val);
            list1 = list1 -> next;
        }
        while (list2 != NULL){
            s.push_back(list2 -> val);
            list2 = list2 -> next;
        }
        sort(s.begin(), s.end());
        ListNode* result = NULL;
        for (int i = 0; i<s.size(); i++){
            push(&result, s[s.size() - 1 - i]);
        }
        return result;
    }
};