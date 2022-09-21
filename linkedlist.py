#Implenting a Singly LinkedList


# The primary operations which are generally a part of the LinkedList class are listed below:

# get_head() - returns the head of the list
# insert_at_tail(data) - inserts an element at the end of the linked list
# insert_at_head(data) - inserts an element at the start/head of the linked list
# delete(data) - deletes an element with your specified value from the linked list
# delete_at_head() - deletes the first element of the list
# search(data) - searches for an element with the specified value in the linked list
# is_empty() - returns true if the linked list is empty


from email import header
from email.errors import NoBoundaryInMultipartDefect
from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    
    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def print_list(self):
        if (self.is_empty()):
            print("List is empty")
            return False
        temp = self.head
        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data, "-> None")
        return True

    def insert_at_head(self, data):

        #create a temp node to link to head

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        return self.head

    def insert_at_tail(lst, data):

        #check if list is empty first and if True add it to head and return

        new_node = Node(data)
        if lst.get_head() is None:
            lst.head = new_node

            return 

    #if list is not empty traverse the list till end by first getting the head

        temp = lst.get_head()
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        new_node = None
        
        return
        
    def insert_at_index(lst, indx, data):

        new_node = Node(data)
        if lst.get_head() is None:
            lst.head = new_node
            return

        #Iterate through list upto index 
        temp = lst.get_head()

        for i in range(indx-1):
            temp = temp.next

        new_node.data = data        
        new_node.next = temp.next
        temp.next = new_node
        
        return

    def search(lst, value):

        temp = lst.get_head()

        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        
        return False
 
    def remove_duplicates(lst):  #sorted LinkedList

        current_node = lst.get_head()
    
        while current_node:
            next_node = current_node.next
            while next_node is not None and next_node.data == current_node.data:
                next_node = next_node.next
            
            current_node.next  = next_node
            current_node = next_node
        return

            



           

lst = LinkedList()
# lst.print_list()


# print("Inserting values in list")
# for i in range(1, 10):
#     lst.insert_at_head(i)
# lst.print_list()

# lst.insert_at_index(4, 800)
# lst.print_list()

# print(lst.search(3))
# lst.insert_at_index(0, 500)
# lst.print_list()


# lst.print_list()
lst.insert_at_tail(6)
lst.insert_at_tail(6)
lst.insert_at_tail(5)
lst.insert_at_tail(4)
lst.insert_at_tail(4)
lst.insert_at_tail(3)
lst.insert_at_tail(3)
lst.print_list()
lst.remove_duplicates()
lst.print_list()
# lst.print_list()
# lst.insert_at_tail(2)
# lst.print_list()
# lst.insert_at_tail(900)
# lst.print_list()




        


    


        