class Queue:
    def __init__(self,size) -> None:
        self.data = []
        self.front = 0
        self.end = 0
        self.size = size

    def enQueue (self,data):
        self.data.insert(self.end,data)
        if self.end > self.size:
            self.end = 0
        else:
            self.end += 1

    def deQueue (self):
        output = self.data[self.front]
        if self.front > self.size:
            self.front = 0
        else:
            self.front += 1
        return output

    def show (self):
        return str(self.data) + str(self.front) + str(self.end)



    def check_length (self):
        if len(self.data) < self.size:
            return True
        else:
            return False
    

def demo():
    q = Queue(2)
    q.enQueue(10)
    print(q.show())
    q.enQueue(45)
    print(q.show())
    print(q.deQueue())
    print(q.show())
    print(q.deQueue())
    q.enQueue(88)
    print(q.show())
    q.enQueue(98)
    print(q.show())

demo()    