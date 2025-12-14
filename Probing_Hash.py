# Probing (aka Closed Addressing, Open hashing), works by squentially added the current element
# in the first empty bucket starting from its hash value


class Phone_Contact:
    def __init__(self, contact_length=64):
        self.contact_length = contact_length
        self.table = [None] * contact_length

        self._DELETED = True # deleted flag
        
        self.load_factor_limit = 0.75
        self.added = 0 #Number of inserted names

    def get_index(self, name):
        found_it = False # did the value exist in the table?

        key = hash(name) % self.contact_length
        first_available = None # Fist Available Pucket To put the value (phone number) in it
        for _ in range(self.contact_length):
            # start from the acutal index
            cur_item = self.table[key]
            if cur_item is None or cur_item == self._DELETED:
                if not first_available:
                    first_available = key
            
            if cur_item[0] == name:
                found_it = True
                return key, found_it

            key = (key + 1) % self.contact_length
        
        # If not found 
        return first_available, found_it
        







    def __setitem__(self, name, phone):
        assert self.added < self.contact_length , 'Full Contact!'

        key_avaliable, found_it = self.get_index(name)
        self.table[key_avaliable] = (name, phone)
        self.added += not found_it

    def remove(self, name):
        assert self.added > 0, 'Empty Table'
        key_avaliable, found_it = self.get_index(name)

        if not found_it:
            return "Not Exist"
        
        self.table[key_avaliable] = self._DELETED
        self.added -= 1

    
    def exist(self, name):
        assert self.added > 0, 'Empty Table'
        _, found_it = self.get_index(name)
        return found_it

    def __getitem__(self, name):
        assert self.added > 0, 'Empty Table'
        key_avaliable, found_it = self.get_index(name)
        if not found_it:
            return "Not Exist"
        
        return self.table[key_avaliable][1]


    


    


