# Linear Search - Count Occurrences of target

def linear(a, t):
    c = 0
    for x in range(len(a)):
        if t == a[x]:
            c += 1
    return c
n = int(input("Enter no. of elements: "))
a = []
for x in range(n):
    a.append(int(input(f"Enter {x+1} element: ")))
t = int(input("Enter the target element: "))
print(linear(a, t))
