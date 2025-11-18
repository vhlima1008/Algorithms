class fullQueueException(Exception): # class that are receiving the exceptions
    pass

class emptyQueueExecption(Exception): # class that are receiving the exceptions
    pass

class Queue: # initializing the class.
    def __init__(self, maxLen=10):
        self._arr = []
        self._maxLen = maxLen

    def insert(self, value):
        if self.full():
            raise fullQueueException("Can't add more: full queue.")
        self._arr.append(value)

    def remove(self):
        if self.empty():
            raise emptyQueueExecption("Can't remove more: empty queue.")
        return self._arr.pop(0)

    def full(self):
        return self.size() == self._maxLen

    def empty(self):
        return len(self._arr) == 0

    def size(self):
        return len(self._arr)

    def __str__(self):
        return f"Queue: {self._arr} (size: {self.size()}/{self._maxLen})"

if __name__ == "__main__": #remembered this initialization from CustomTKinter.

    while True:
        try:
            print("Initializing your queue...")
            maxSize = int(input("Write the max size of your queue: "))
            if maxSize > 0:
                print(f"Choosed {maxSize} as max size.")
                Queue = Queue(maxSize)
                print(f"Initialized the Queue with","\n",Queue)
                break
            else:
                raise ValueError("Maximium lenght need to be greater than 0.")
        except (ValueError) as e: # I got this reference from CustomTKinter setup for raise and show the program exceptions.
            print("Error:", e)

    while True:
        print("\nChoose one option: ")
        print("1 - insert")
        print("2 - remove")
        print("3 - show queue")
        print("4 - quit")

        opt = input("Option: ")

        try:
            if opt == "1":
                value = input("Insert a value: ")
                Queue.insert(value)
                print(f"Inserted!","\n",Queue)

            elif opt == "2":
                removed = Queue.remove()
                print(f"Removed: {removed}","\n",Queue)

            elif opt == "3":
                print(Queue)

            elif opt == "4":
                print("Bye...")
                break

            else:
                print("Invalid choose!")

        except (fullQueueException, emptyQueueExecption, ValueError) as e: # one more time I got this reference from CustomTKinter setup for raise and show the program exceptions.
            print("Error:", e)

# by Victor Hugo Lima