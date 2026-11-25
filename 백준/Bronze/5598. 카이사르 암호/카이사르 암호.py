word = input()
arr = []
for w in word:
    a = ord(w)
    if a >= 68:
        arr.append(chr(a - 3))
    else:
        arr.append(chr(a + 23))
print(''.join(arr))