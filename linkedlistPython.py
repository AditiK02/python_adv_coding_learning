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

