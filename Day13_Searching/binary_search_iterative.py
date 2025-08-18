# Binary Search - Iterative approach
# Works only if the array is sorted

a = [2, 5, 8, 10, 15, 20]
t = 10
low = 0
high = len(a) - 1
while low <= high:
    mid = (low + high) // 2
    if t == a[mid]:
        print("Element found at index:", mid)
        break
    elif a[mid] < t:
        low = mid + 1
    else:
        high = mid - 1
      
