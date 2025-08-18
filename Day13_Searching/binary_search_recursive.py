# Binary Search - Recursive approach
# Works only if the array is sorted

def binary_search(a, low, high, t):
    if low <= high:
        mid = (low + high) // 2
        if a[mid] == t:
            return mid
        elif a[mid] < t:
            return binary_search(a, mid+1, high, t)
        else:
            return binary_search(a, low, mid-1, t)
    return -1

a = [2, 5, 8, 10, 15, 20]
t = 10
result = binary_search(a, 0, len(a)-1, t)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
