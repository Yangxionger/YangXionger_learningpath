//反转链表 原地反转 三指针 prev cur next
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
       ListNode* prev=nullptr;
       ListNode* cur=head;
       ListNode* next;
       while(cur){
        next=cur->next;
        cur->next=prev;
        prev=cur;
        cur=next;
       }
       return prev;
    }
};