string = input()

empty_set = set()


for i in range(len(string)):
    if string[i] not in empty_set:
        print(f"{string[i]} {string.count(string[i])}")
        empty_set.add(string[i])
