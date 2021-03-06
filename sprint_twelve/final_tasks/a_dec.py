"""
ID 68489898
"""
class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value: int):
        if self.size != self.max_n:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value: int):
        if self.size != self.max_n:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        qt = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return qt

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        qh = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return qh


def main():
    queue = Queue(m)
    commands = {
        'push_front': queue.push_front,
        'push_back': queue.push_back,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back
    }

    for _ in range(n):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                print(commands[operation])
                result = commands[operation](int(*value))
                if result is not None:
                    print(result)
            except OverflowError:
                print('error')
        else:
            try:
                result = commands[operation]()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    main()
# command = (queue.push_back(input().split()) for _ in range(m))