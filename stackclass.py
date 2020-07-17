class StackClass:

    NOELEMENTS = "The stack does not have elements."
    
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)
        return "Added item to the stack."

    def pop(self):
        if self.items:
            return self.items.pop()

        return self.NOELEMENTS

    def peek(self):
        if self.items:
            return self.items[-1]

        return self.NOELEMENTS

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items==[]
    