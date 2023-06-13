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


    

def demo():
    q = Queue(2)
    q.enQueue(10)
    q.enQueue(45)
    print(q.deQueue())
    print(q.deQueue())
    q.enQueue(88)
    q.enQueue(98)
