class CustomList:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity  

    def append(self, element):
        self.array[self.size] = element
        self.size += 1
        print(f"Appended {element} to the list")

    def resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity 
        self.array = new_array  

    def get(self, index):
        print(f"Element at index {index}: {self.array[index]}")

    def set(self, index, element):
        print(f"Set element at index {index} to {element}")

    def get_size(self):
        return self.size  


answer = CustomList()
answer.append(5)
answer.get(0)
answer.set(0, 10)
print(f"Current size: {answer.get_size()}")