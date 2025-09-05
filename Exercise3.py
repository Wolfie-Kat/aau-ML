

def func(string):
    
    string = string.lower()
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

x = "AaaBB"
result = func(x)
print(result)
