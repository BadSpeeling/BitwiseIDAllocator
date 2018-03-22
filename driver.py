#A simple ID allocator.  Makes use of bitwise functions to perform actions in O(1) time
class IDAllocator ():

    def __init__ (self,amt_ids):
        self.max = 2**amt_ids-1
        self.ids = 0
    
    #returns None if id is in use or not a valid id, ID assigned if the allocation is sucessful
    def alloc (self, new_id):
        if (new_id < 0 or self.max < 2**new_id or ((self.ids >> new_id) % 2 == 1)):
            return None
        self.ids += 2**new_id
        return new_id
    
    def dealloc (self, rem_id):
        if (rem_id < 0 or self.max < 2**rem_id or ((self.ids >> rem_id) % 2 == 0)):
            return None
        self.ids -= 2**rem_id
        return rem_id
    
