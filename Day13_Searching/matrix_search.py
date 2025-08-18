# Search for a target element in a 2D matrix

def matrix(k, l, t):
    mat = []
    for x in range(k):
        row_var = []
        for y in range(l):
            row_var.append(int(input(f"Enter the element in {x},{y}: ")))
        mat.append(row_var)
    m = []
    for a in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[a][x] == t:
                m.append((a, x))
    return m
rows = int(input("Enter no. of rows: "))
cols = int(input("Enter no. of columns: "))
t = int(input("Enter the target element: "))
print(matrix(rows, cols, t))
