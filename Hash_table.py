class Hash_table:
    def __init__(self) -> None:
        self.data = []
    
    def add(self,data):
        index = data // 5
        self.data.insert(index,data)

    def remove(self,data):
        self.data.remove(data)

    def check(self,data):
        index = data // 5
        if self.data[index] == data:
            return True
        else:
            return False

    def show(self):
        return self.data

def demo():
    h = Hash_table()
    print(h.show())
    h.add(10)
    print(h.show())
    h.add(45)
    print(h.show())
    h.add(88)
    print(h.show())
    h.remove(45)
    print(h.show())
    h.check(88)

demo()