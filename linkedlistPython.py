class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None

    def insert_in_between_at_position(self,data,position):
        new_node=Node(data)

        temp=self.head
        count=0
        while count<position:
            prev=temp
            temp=temp.next
            count+=1
        prev.next=new_node
        new_node.next=temp

    def delete_node_at_position(self,position):
        temp=self.head
        count=0
        while count<position:
            prev=temp
            temp=temp.next
            count+=1
        prev.next=temp.next
        temp=None

    def searching_key(self,key):
        temp=self.head
        count=0
        while temp:
            count+=1
            if temp.data==key:
                return count
            temp=temp.next
        return False    
    
    def reverse_linkedlist(self):
        prev=None
        current=self.head
        while current:
            new_node=current.next
            current.next=prev
            prev=current
            current=new_node
        self.head=prev    
    
    def cycle_found_floyd(self):
        fast=slow=self.head
        current=self.head
        while current and current.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True   #it contains cycle
        return False    # No cycle
    

    def linkedlist_palindrome_using_stack(self):
        # 1->2->3->2->1
        # 1->2->3->3->2->1 this is also palindrome since two halves mirror each other
        slow=fast=self.head
        stack=[]
        while fast and fast.next:
            stack.append(slow.data)
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next # for odd linkedlist -- cuz fast wont go to None in odd case

        while slow:
            top= stack.pop()
            if top!=slow.data:
                return False
            slow=slow.next
        
        return True    


    #Another method for linkedlist palindrome
    def linkedlist_palindrome_using_reverse_linkedlist(self):
        slow=fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second_half=self._reverse_for_palindrome(slow)
        first_half=self.head
        while second_half:
            if first_half.data!=second_half.data:
                return False
            second_half=second_half.next
            first_half=first_half.next
        return True    


    def _reverse_for_palindrome(self,head): #method of palindrome
        prev=None
        current=head
        while current:
            newnode=current.next
            current.next=prev
            prev=current
            current=newnode
        head=prev    
    

    def middle_of_linkedlist(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow


           

list1=linkedlist()
list1.insert_at_begining(4)
list1.insert_at_end(5)
list1.insert_at_end(9)
list1.insert_at_end(7)
list1.display()
print("--------------")
list1.insert_in_between_at_position(12,3)
list1.display()
print("--------------")
list1.display()
pos=list1.searching_key(9)
print("key is found at :",pos)

