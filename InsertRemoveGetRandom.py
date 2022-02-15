import random

#O(n)
class PromoCode():
    def __init__(self):
        self.codes = []
        self.code2idx = {}
        self.count = 0

    def insert(self,code):
        self.codes.append(code)
        self.code2idx[code] = self.count
        self.count +=1
    
    def remove(self,code) -> bool:
        i = self.code2idx.get(code)
        if i is None:
            return False
            
        last_i = self.count-1
        self.codes[i], self.codes[last_i]=self.codes[last_i], self.codes[i]
        self.code2idx[self.codes[i]]=i
        del self.code2idx[code]
        self.codes.pop()
        self.count -= 1
        return True

    def getRandom(self) ->int:
        if len(self.codes)==0:
            return -1
        i = random.randint(0, len(self.codes)-1)
        return self.codes[i]

pc = PromoCode()

print(pc.remove(1), False)
print(pc.getRandom(), -1)

pc.insert(1)
pc.insert(2)
pc.insert(3)


print([pc.getRandom() for _ in range(10)])
pc.remove(3)
print([pc.getRandom() for _ in range(10)])
pc.remove(2)
print([pc.getRandom() for _ in range(10)])
pc.remove(1)


print(pc.remove(1),False)
print(pc.getRandom(),-1)