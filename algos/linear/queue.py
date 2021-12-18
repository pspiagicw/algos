from algos.linear.dynamic import DynamicArray


class Queue(DynamicArray):
    """The main Queue class"""
    def queue(self, value):
        self.append(value)

    def dequeue(self, value):
        start_value = self.array[0]
        self.remove(0)
        return start_value
