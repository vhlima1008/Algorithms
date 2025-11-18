from typing import Any, Optional


# Exceptions
class FullQueueException(Exception): # inserted into a full queue
    pass


class EmptyQueueException(Exception): # removing from a empty queue
    pass


# Node
class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None


# Queue
class Queue:
    def __init__(self, maxLen: int = 10):
        self._head: Optional[Node] = None  # points to the first element
        self._tail: Optional[Node] = None  # points to the last element
        self._maxLen: int = maxLen
        self._size: int = 0

    def insert(self, value: Any) -> None:
        if self.full():
            raise FullQueueException("Can't add more: full queue.")
        new_node = Node(value)
        if self._tail is None:
            # Empty queue | head and tail point to the new node
            self._head = self._tail = new_node
        else:
            # Link the current tail to the new node
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def remove(self) -> Any:
        if self.empty():
            raise EmptyQueueException("Can't remove more: empty queue.")
        assert self._head is not None
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None  # queue became empty
        self._size -= 1
        return value

    def full(self) -> bool:
        return self._size == self._maxLen

    def empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def __str__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(repr(current.value))
            current = current.next
        return f"Queue[front -> {' -> '.join(values)}] (size: {self._size}/{self._maxLen})"


if __name__ == "__main__":
    while True:
        try:
            print("Initializing your queue...")
            maxSize = int(input("Write the max size of your queue: "))
            if maxSize > 0:
                print(f"Chosen {maxSize} as max size.")
                queue = Queue(maxSize)
                print(f"Initialized the Queue:\n{queue}")
                break
            else:
                raise ValueError("Maximum length must be greater than 0.")
        except ValueError as e:
            print("Error:", e)

    while True:
        print("\nChoose one option:")
        print("1 - insert")
        print("2 - remove")
        print("3 - show queue")
        print("4 - quit")

        opt = input("Option: ")

        try:
            if opt == "1":
                value = input("Insert a value: ")
                queue.insert(value)
                print(f"Inserted!\n{queue}")

            elif opt == "2":
                removed = queue.remove()
                print(f"Removed: {removed}\n{queue}")

            elif opt == "3":
                print(queue)

            elif opt == "4":
                print("Bye...")
                break

            else:
                print("Invalid choice!")

        except (FullQueueException, EmptyQueueException, ValueError) as e:
            print("Error:", e)
