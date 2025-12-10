# Chaining (aka Open Addressing, closed hashing), works by adding another Data Structure
# in each bucket to store the values with the same hash values (Collision!)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Linked_List:
    def __init__(self, head=None):
        if head:
            head = Node(head)

        self.head = head
        self.tail = head

    def append(self, value):
        new_node = Node(value)
        if not self.head: # Empty LL
            self.head = new_node
            self.tail = new_node
        
        elif self.head == self.tail: # Only One Value
            self.head.next = new_node
            self.tail = new_node
        
        else: # More Than One
            self.tail.next = new_node
            self.tail = new_node



class Phone_Contact:
    def __init__(self, length_contacts):
        self.length = length_contacts # Maximum Number Of Contacts
        self.table = [None] * length_contacts


    # Let's hasing 
    def __setitem__(self, name, phone_number):
        idx = hash(name) % self.length # Comperssion
        print(f'IDX [{idx}] FOR {name}')
        
        if self.table[idx]: # Collision
            self.table[idx].append((name, phone_number))

        else:
            self.table[idx] = Linked_List((name, phone_number))

    def __getitem__(self, name):
        idx = hash(name) % self.length
        if not self.table[idx]: # Not Exist
            return "Name Is Not In Your Contact!"
        
        else:
            list_names = self.table[idx]

            # Search in the Linked List About the Value
            cur_node = list_names.head

            while cur_node:
                name_in_list, phone = cur_node.val
                if name == name_in_list:
                    return name, phone
                
                cur_node = cur_node.next
            return "Not Found"


my_contact = Phone_Contact(2)
my_contact['Mohamed'] = 1063557194
my_contact['Ahmed'] = 323134
my_contact['Kareem'] = 31114

print(my_contact['Kareem']) 
print(my_contact['Mohamed'])
print(my_contact['Ahmed'])
print(my_contact['Mona']) # Not Exist


    
