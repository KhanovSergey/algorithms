import random
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    __slots__ = ['username', 'solved', 'errors']
    username: str
    solved: int
    errors: int

#   Такой компаратор лучше сделать на основе сравнения ключа
#   В качестве ключа может использоваться кортеж
#
#   def key(self):
#       return (-self.solved, self.errors, self.username)
#
#   def __gt__(self, other):
#       return self.key() > other.key()

    def __gt__(self, other):
        if self.solved == other.solved:
            return self.username > other.username if self.errors == other.errors else self.errors > other.errors
        return self.solved < other.solved

    def __lt__(self, other):
        return other > self

    def __str__(self):
        return self.username


def quicksort(arr, low, high):
    if low >= high:
        return -1

    left, right = low, high
    pivot = arr[random.randint(low, high)]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quicksort(arr, low=low, high=right)
    quicksort(arr, low=left, high=high)


n = int(input())
users = []

for _ in range(n):
    username, solved, errors = input().split()
    users.append(User(username, int(solved), int(errors)))

quicksort(users, low=0, high=n-1)

for person in users:
    print(person)


# def partition(competitors, left, right):
#     pivot = (competitors[left])
#     i = left + 1
#     j = right - 1
#     while True:
#         if (i <= j and competitors[j] > pivot):
#             j -= 1
#         elif (i <= j and competitors[i] < pivot):
#             i += 1
#         elif (competitors[j] > pivot) or (competitors[i] < pivot):
#             continue
#         if i <= j:
#             competitors[i], competitors[j] = competitors[j], competitors[i]
#         else:
#             competitors[left], competitors[j] = competitors[j], competitors[left]
#             return j
# def quick_sort(competitors, left, right):
#     if ((right - left) > 1):
#         p = partition(competitors, left, right)
#         quick_sort(competitors, left, p)
#         quick_sort(competitors, p + 1, right)
# def transformation(competitors):
#     competitors[1] = - int(competitors[1])
#     competitors[2] = int(competitors[2])
#     return [competitors[1], competitors[2], competitors[0]]
# if __name__ == '__main__':
#     number = int(input())
#     competitors = [transformation(input().split()) for _ in range(number)]
#     left = 0
#     quick_sort(competitors, left, len(competitors))
#     print(*(list(zip(*competitors))[2]), sep="\n")