# Linear Search - Basic (Check if element exists)

def linear(a, t):
    for x in range(len(a)):
        if t == a[x]:
            return "Yes"
    return "No"
n = int(input("Enter no. of elements: "))
a = []
for x in range(n):
    a.append(int(input(f"Enter {x+1} element: ")))
t = int(input("Enter the target element: "))
print(linear(a, t))
