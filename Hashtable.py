
#Author: Nabeel Aref
#Student ID: 010199591
#Project: C950 WGUPS Routing Program


# Hashtable Class
class Hashtable:

    #Constructor for the hashtable. O(1)
    def __init__(self):
        self.table_size = 40
        
        self.table_map = []
        for i in range(0,40):self.table_map.append(None)
    # Used when adding values and packages to the hashtable.
    def add_item(self, key, value):
        item = [key, value]

        hash = self.generate_hash(key)
        if self.table_map[hash] == None:
            self.table_map[hash] = [item]
            return True
        for i in self.table_map[hash]:
            if i[0] == key:
                i[1] = value
                return True
            self.table_map[hash].append(item)
            return True
    #Gets hash.
    def generate_hash(self, key):
        tablehash = 0
        for char in str(key):tablehash = tablehash+ ord(char)
        return tablehash % self.table_size

        #Removes an item from the structure.

    def remove_item(self, key):
        hash = self.generate_hash(key)
        if self.table_map[hash] == None: return False
        for i in range(0, len(self.table_map[hash])):
            if self.table_map[hash][i][0] == key:
                self.table_map[hash].pop(i)
                return True

    #The look-up function, which is used to search for a particular item in a hash table.
    def get_item(self, key):
        hash = self.generate_hash(key)
        if self.table_map[hash] != None:
            for i in self.table_map[hash]:
                if key == i[0]:
                    return i[1]
        return None

    # # print function that will print all items in data structure
    # def print(self):
    #     print('-'*4 + 'all packages' + '-'*4)
    #     for item in self.table_map:
    #         if item != None:print(str(item))


