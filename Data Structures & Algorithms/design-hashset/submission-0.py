class MyHashSet:

    def __init__(self):
        self.container = set()

    def add(self, key: int) -> None:
        con = self.container
        con.add(key)
        print("Successful!")
        

    def remove(self, key: int) -> None:
        con = self.container
        con.discard(key)
        

    def contains(self, key: int) -> bool:
        con = self.container
        if key in con:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)