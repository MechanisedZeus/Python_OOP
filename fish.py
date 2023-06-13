class Animal:
    def __init__(self,s,n) -> None:
        self.state = s
        self.size = n
        
    def feed(self):
        self.size = self.size + 1
        if self.size == 5:
            self.state = "FISH"

    def get_state(self):
        return self.state

    def get_size(self):
        return self.size



fish1 = Animal("fish", 1)

print(fish1.get_state())
print("the size of the fish is",fish1.get_size())

while fish1.get_state() != "FISH":
    fish1.feed()

print("It is now a big")
print(fish1.get_state())
