class Set:
    def __init__(self, value=[]):  # Constructor
        self.data = []  # Manages a list
        self.concat(value)

    def intersection(self, other):  # other is any sequence
        res = []  # self is the subject
        for x in self.data:
            if x in other:  # Pick common items
                res.append(x)
        return Set(res)  # Return a new Set

    def union(self, other):  # other is any sequence
        res = self.data[:]  # Copy of my list
        for x in other:  # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def issubset(self, other):
        for x in self.data:
            if x in other.data:
                continue
            else:
                return False
        if(len(self.data) == len(other.data)):
            return "self <= other"
        else:
            return "self < other"

    def issuperset(self, other):
        for x in other:
            if x in self.data:
                continue
            else:
                return False
        if(len(self.data) == len(other.data)):
            return 'self >= other'
        else:
            return 'self > other'

    def union_update(self, other):
        #self |= other, adding elements from all others
        temp = [x for x in other.data if x not in self.data]
        self.data += temp
        return self

    def intersection_update(self, other):
        #self &= other, only elements found in it and all others
        self.data = [x for x in self.data if x in other.data]
        return self

    def difference_update(self, other):
        #self -= other, removing elements found in others
        self.data = [x for x in self.data if x not in other.data]
        return self

    def symmetric_difference_update(self, other):
        #self^= other
        inter = [x for x in self.data if x in other.data]
        temp = [x for x in other.data if x not in self.data]
        union = self.data + temp
        self.data = [x for x in union if x not in inter]
        return self

    def add(self, elem):
        if elem not in self.data:
            self.data.append(elem)
        return self

    def remove(self, elem):
        if elem in self.data:
            idx = self.data.index(elem)
            self.data = self.data[0:idx] + self[idx+1:]
            return self
        else:
            raise KeyError(f'{elem}' " is not in data")

    def concat(self, value):
        for x in value:
            if not x in self.data:  # Removes duplicates
                self.data.append(x)

    def __len__(self):
        return len(self.data)  # len(self)

    def __getitem__(self, key):
        return self.data[key]  # self[i], self[i:j]

    def __and__(self, other):
        return self.intersection(other)  # self & other

    def __or__(self, other):
        return self.union(other)  # self | other

    def __repr__(self):
        return 'Set({})'.format(repr(self.data))

    def __iter__(self):
        return iter(self.data)  # for x in self:


x = Set([1, 3, 5, 7, 1, 3]) #[1,3,5,7]
y = Set([2, 1, 4, 5, 6]) #[1,2,4,5,6]
print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x & y, x | y)
print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))  # convert to list because x is iterable

print("issubset: ", x.issubset(y))
print("issuperset: ", x.issuperset(y))
print("union_update: ", x.union_update(y))

x = Set([1, 3, 5, 7, 1, 3]) #[1,3,5,7]
print("intersection_update: ", x.intersection_update(y))

x = Set([1, 3, 5, 7, 1, 3]) #[1,3,5,7]
print("difference_update: ", x.difference_update(y))

x = Set([1, 3, 5, 7, 1, 3]) #[1,3,5,7]
print("symmetric_difference_update: ", x.symmetric_difference_update(y))

x = Set([1, 3, 5, 7, 1, 3]) #[1,3,5,7]
print("add: ", x.add(9))

x = Set([1, 3, 5, 7, 1, 3]) #[1,3,5,7]
print("remove: ", x.remove(1)) #raise Key error

x = Set([1, 3, 5, 7, 1, 3]) #[1,3,5,7]
x.remove(8) #raise Key error