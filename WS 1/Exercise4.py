

def func(sentence):
    reverse = ""
    i = len(sentence)
    while i:
        i -= 1
        reverse += sentence[i]
    if reverse.lower() == sentence.lower():
        print("\nThis is a palindrome!\n")
    return reverse

x = "Katrine"
result = func(x)
print("Reverse of", x, "is", result)