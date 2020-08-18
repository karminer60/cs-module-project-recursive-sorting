# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    initial = 0
    last = len(arr) - 1
    

    while initial <= last:
        mid = (initial  + last) // 2
       
        if arr[mid] < target:
            initial = mid + 1

        elif arr[mid] > target:
            last = mid - 1
        else:
            return mid    

    return -1  # not found

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

