

def func(x, y):
    index = -1

    for i in range(len(y)):
        for j in range(len(x)):
            if x[j] == y[i]:
                index = i
                break
    return index

x = "doors"
y = "test"
print(func(x, y))