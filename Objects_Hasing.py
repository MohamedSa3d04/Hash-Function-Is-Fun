class ContactInfo:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    
    def get_hash(self):
        keys = (self.name, self.phone)
        return hash(keys)
    
    def __hash__(self):
        keys = (self.name, self.phone)
        return hash(keys)
    

    def __eq__(self, other_obj):
        return self.name == other_obj.name and \
        self.phone == other_obj.phone
    
p1 = ContactInfo('Mohamed', 'SA', 211)
p2 = ContactInfo('Mohamed', 'EG', 211)
print(p1.get_hash())
print(p2.get_hash())

print(hash(p1))
print(hash(p2))
print(p1 == p2)
