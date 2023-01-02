/*
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    Input: head = [1], n = 1
    Output: []

    Input: head = [1,2], n = 1
    Output: [1]
*/

#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

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
    int get_size(ListNode* head){
        int size = 0;
        while (head != NULL){
            size++;
            head = head -> next;
        }
        return size;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == NULL)   return head;
        
        int pos = get_size(head) - n;
        ListNode *temp = head;
        if (pos == 0){
            head = temp -> next;
            delete temp;
            return head;
        }

        // Find previous node of the node to be deleted
        for (int i = 0; i<pos-1; i++)   temp = temp->next;
        if (temp != NULL){
            ListNode *next = (temp->next) -> next;
            delete temp->next;
            temp->next = next;
        }
        return head;
    }
};