# Linear Search - Return all indices of target element

def linear(a, t):
    c = []
    for x in range(len(a)):
        if t == a[x]:
            c.append(x)
    return c if c else -1
n = int(input("Enter no. of elements: "))
a = []
for x in range(n):
    a.append(int(input(f"Enter {x+1} element: ")))
t = int(input("Enter the target element: "))
print(linear(a, t))
