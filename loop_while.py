#loop_while.py
i = 0

while i < 7:
    i += 1
    if i == 3 or i == 4:
        continue
    if i == 5:
        break
    print(i)

print(i)    