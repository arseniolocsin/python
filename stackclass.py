class StackClass:

    NOELEMENTS = "The stack does not have elements."
    
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)
        msg = "Added " + item + " to the stack."
        print(msg)
        return None
        # return "Added item to the stack."

    def pop(self):
        if self.items:
            topitem = self.peek()
            msg = topitem + " is on top of the stack."
            print(msg)
            self.items.pop()
            msg = "Removed " + topitem + " from the stack."
            print(msg)
            return None

        return self.NOELEMENTS

    def peek(self):
        if self.items:
            return self.items[-1]

        return self.NOELEMENTS

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items==[]

    # Test Module
    test = StackClass()
    test.push("Apple")
    test.push("Orange")
    