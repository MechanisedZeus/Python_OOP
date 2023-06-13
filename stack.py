class Stack:
    def __init__(self,length) -> None:
        self.data = []
        self.top = 0
        self.length = length
        
    def stack(self,data):
        if self.check_length():
            self.data.insert(self.top,data)
            self.top += 1
        else:
            print("The stack is full, pop some data and try again")

    def pop(self):
        self.top -= 1
        return self.data.pop()

    def get_top(self):
        return self.top

    def poke(self):
        return self.data[self.top-1]
    
    def check_length(self):
        if len(self.data) < self.length:
            return True
        else:
            return False

def demo():
    st = Stack(5)
    st.stack(10)
    st.stack(45)
    st.stack(88)
    print(st.poke())
    print(st.get_top())
    print(st.pop())
    print(st.poke())
    print(st.check_length())
