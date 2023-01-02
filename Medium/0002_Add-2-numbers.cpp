/*
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
*/

#include <bits/stdc++.h>
using namespace std;
#define MAX_INPUT_LENGTH     100
#define ll long long

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

    void add_Node(struct ListNode **head, int n){
        ListNode* new_node = new ListNode();
        ListNode *last = *head;
        new_node->val = n;
        new_node->next = NULL;
        if (*head == NULL){
            *head = new_node;
            return;
        }
        while (last->next != NULL)  last = last->next;
        last->next = new_node;
        return;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* long_list = (get_size(l1) > get_size(l2)) ? l1 : l2;
        ListNode* short_list = (get_size(l1) <= get_size(l2)) ? l1 : l2;
        int len_dif = get_size(long_list) - get_size(short_list);
        for (int i = 0; i<len_dif; i++) add_Node(&short_list, 0);

        ListNode* result = NULL;
        int temp, n = 0;
        while (long_list != NULL){
            temp = long_list->val + short_list->val + n;
            if (temp > 9){
                temp %= 10;
                n = 1;
            }
            else    n = 0;
            add_Node(&result, temp);
            long_list = long_list -> next;
            short_list = short_list -> next;
        }
        if (n == 1) add_Node(&result, 1);
        return result; 
    }
};