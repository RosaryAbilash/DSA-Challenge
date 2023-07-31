nums = list(map(int, input("Enter List: ").split()))
target = int(input("Enter a Target to search: "))


def binary_search(nums, target):
    low = 0
    high = len(nums)-1
    while(low < high):
        mid = low + ((high-low+1)//2)
        if (target < nums[mid]):
            high = mid - 1
        else:
            low = mid
    if (target == nums[mid]):
        return low
    else:
        return -1


print(f'The Index in the List is {binary_search(nums, target)}')