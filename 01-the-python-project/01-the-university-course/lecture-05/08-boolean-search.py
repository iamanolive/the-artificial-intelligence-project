found = False
print("before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        print(found, value)
        break
    print(found, value)
print("after", found)