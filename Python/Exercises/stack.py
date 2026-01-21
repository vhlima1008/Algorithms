from typing import Any, Optional

# Stack Node
class Node:
    def __init__(self, value: Any, next: Optional["Node"] = None):
        self.value = value
        self.next = next  # reference (pointer) to the next node

# Stack
class Stack:
    def __init__(self):
        self.__top: Optional[Node] = None  # pointer to the top element
        self.__size: int = 0

    # push an element to the top
    def push(self, item: Any) -> None:
        new_node = Node(item, self.__top)
        self.__top = new_node
        self.__size += 1

    # removes and returns the element at the top
    def pop(self) -> Any:
        if self.__top is None:
            raise IndexError("pop from empty stack")
        value = self.__top.value
        self.__top = self.__top.next  # moves the top pointer to the next node
        self.__size -= 1
        return value

    # returns the top element
    def peek(self) -> Any:
        if self.__top is None:
            return None
        return self.__top.value

    # return the visualization
    def __str__(self):
        values = []
        current = self.__top
        while current:
            values.append(repr(current.value))
            current = current.next
        return f"{'\n'.join(values)}"


if __name__ == "__main__":
    stack = Stack()

    stack.push("Harry Potter and The Philosopher's Stone")
    stack.push("The Time Machine")
    stack.push("Crime and Punishment")

    print(stack.pop()) # removes "Crime and Punishment"
    print(stack.pop()) # removes "The Time Machine"

    stack.push("Harry Potter and The Prisioner of Azkaban")
    stack.push("Harry Potter and The Order of The Phoenix")

    print('\n' + f'{stack}')
    print('\n' + f"The last one is: {stack.peek()}", '\n')
