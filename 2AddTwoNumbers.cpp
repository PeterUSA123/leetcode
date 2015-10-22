#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:  
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		int in = 0;
		ListNode* list = new ListNode(0);
		ListNode* head = list;
		ListNode* prev = list;
	
		while(l1 && l2){
			in += l1->val + l2->val;
		
			list = new ListNode(0);
			list->val = in%10;
			in /= 10;
		
			l1 = l1->next;
			l2 = l2->next;
			prev->next = list;
			prev = prev->next;
		}
	
		while(l1){
			in += l1->val;
		
			list = new ListNode(0);
			list->val = in%10;
			in /= 10;
		
			l1 = l1->next;
			prev->next = list;
			prev = prev->next;	
		}
	
		while(l2){
			in += l2->val;
		
			list = new ListNode(0);
			list->val = in%10;
			in /= 10;
		
			l2 = l2->next;
			prev->next = list;
			prev = prev->next;	
		}
		
		if(in){
			list = new ListNode(0);
			list->value_type = in;
			prev->next = list;
			prev = prev->next;
		}
		return head->next;
	}
};  

int main()
{
	return 0;
}
