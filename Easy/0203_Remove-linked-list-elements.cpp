#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

/*
    Given the head of a linked list and an integer val, 
    remove all the nodes of the linked list that has Node.val == val, and return the new head.

    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

    Input: head = [], val = 1
    Output: []

    Input: head = [7,7,7,7], val = 7
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
    ListNode* Clone(ListNode* head){
        if (head == NULL)   return NULL;
        ListNode* result = new ListNode;
        result -> val = head -> val;
        result -> next = Clone(head->next);
        return result;
    }
    
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* one = NULL;
        ListNode* two = NULL;
        while (head != NULL){
            if (head -> val != val){
                if (one == NULL){
                    one = new ListNode;
                    one -> val = head -> val;
                    one -> next = NULL;
                    two = one;
                }
                else{
                    two -> next = new ListNode;
                    two = two -> next;
                    two -> val = head -> val;
                    two -> next = NULL;
                }
            }
            head = head->next;
        }
        return one;    
    }
};