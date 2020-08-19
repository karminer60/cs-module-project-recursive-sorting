# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
        mid = (start  + end) // 2

        if end == -1:
            return -1

        if arr[mid] == target:
            return mid

        if start == end:
            return -1

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1
        
        return binary_search(arr, target, start, end)
        

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

