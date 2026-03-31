class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        sum_of_chars = 0
        for char in string:
            sum_of_chars += ord(char)
        return sum_of_chars 
     
    def add(self, key, value):
        index = self.hash(key)
        if index not in self.collection:
            self.collection[index] = {} 
        self.collection[index][key] = value
    
    def remove(self, key):
        index = self.hash(key)
        if index in self.collection and key in self.collection[index]:
            del self.collection[index][key]

    def lookup(self, key):
        index = self.hash(key)
        if index in self.collection and key in self.collection[index]:
            return self.collection[index][key]
        return None
