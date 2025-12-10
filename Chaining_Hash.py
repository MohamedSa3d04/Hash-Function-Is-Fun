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

        self.load_factor_limit = 0.75 # Default of Java (n_string / table_size)
        self.added = 0


    # Let's hasing 
    def __setitem__(self, name, phone_number):
        idx = hash(name) % self.length # Comperssion
        print(f'IDX [{idx}] FOR {name}')
        
        if self.table[idx]: # Collision
            # check if the same name -> reassign
            cur_node = self.table[idx].head
            while cur_node:
                name_in_list, _ = cur_node.val
                if name_in_list == name:
                    # Update instead of adding another entry
                    cur_node.val = (name, phone_number)
                    return
                cur_node = cur_node.next
            self.table[idx].append((name, phone_number))

        else:
            self.table[idx] = Linked_List((name, phone_number))

        self.added += 1
        # Check If we exceed the load_factor thresold or not
        if self.added / self.length >= self.load_factor_limit:
            self.rehashing()
         
    def rehashing(self):
        new_length = self.length * 2
        bigger_contact = Phone_Contact(new_length)

        added_contact = filter(lambda bucket: bucket, self.table)
        for list_info in added_contact:
            cur_node = list_info.head
            while cur_node:
                name_in_list, phone = cur_node.val
                bigger_contact[name_in_list] = phone           
                cur_node = cur_node.next

        # Copy new structure into self
        self.length = bigger_contact.length
        self.table = bigger_contact.table
        self.added = bigger_contact.added
        print("Done Rehashing!!")



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
my_contact['Mona'] = 33331
my_contact['Rami'] = 3212

print(my_contact.length, len(my_contact.table))
print(my_contact['Kareem']) 
print(my_contact['Mohamed'])
print(my_contact['Ahmed'])
print(my_contact['Mona']) # Not Exist


    
