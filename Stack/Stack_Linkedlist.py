class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.__size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.__size += 1

    def pop(self):
        if not self.head:
            raise IndexError("Stack Underflow")
        popped_value = self.head.data
        self.head = self.head.next
        self.__size -= 1
        return popped_value

    def peek(self):
        if not self.head:
            raise IndexError("Stack is empty")
        return self.head.data

    def __len__(self):
        return self.__size

    def display(self):
        if not self.head:
            print("Stack is empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.data}", end=" <-> " if temp.next else "\n")
            temp = temp.next

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)  # Successfully inserted 10
    stack.push(90)  # Successfully inserted 90
    print(len(stack))  # 2
    stack.display()  # 90 <-> 10
    print(stack.peek())  # 90
    for i in stack:  # 90, 10
        print(i)
    stack.pop()  # 90
    print(len(stack))  # 1
    stack.display()  # 10
