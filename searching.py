x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

def find_index(x, y1, y2):
    if y1 in x:
        return x.index(y1)
    elif y2 in x:
        return x.index(y2)
    else:
        return 0

output = find_index(x, y1, y2)
print("Output:", output)