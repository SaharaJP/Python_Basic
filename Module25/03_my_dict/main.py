class MyDict(dict):
    def get(self, key):
        if key in self.keys():
            return self[key]
        else:
            return 0


my_dict = MyDict()
my_dict['a'] = 1

print(my_dict.get('b'))
print(my_dict.get('a'))