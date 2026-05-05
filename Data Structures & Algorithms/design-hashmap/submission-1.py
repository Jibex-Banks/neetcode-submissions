class MyHashMap:

    def __init__(self):
        self.container = dict()
        

    def put(self, key: int, value: int) -> None:
        con = self.container
        con[key]=value

    def get(self, key: int) -> int:
        con = self.container
        result = con.get(key)
        return result if result != None else -1
        

    def remove(self, key: int) -> None:
        con = self.container
        if con.get(key) == None:
            return "null"
        del con[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)