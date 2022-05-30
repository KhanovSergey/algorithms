def binary_search(arr, target, low=None, high=None):
    low = 0 if low is None else low
    high = len(arr) - 1 if high is None else high

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_pivot(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid
    return high if high else len(arr) - 1


def broken_search(nums, target):
    pivot = find_pivot(nums)

    if nums[pivot] == target:
        return pivot

    return binary_search(nums, target, high=pivot-1) if nums[0] <= target else binary_search(nums, target, low=pivot+1)
