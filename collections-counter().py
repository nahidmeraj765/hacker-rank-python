x = int(input())  # the number of shoes that the seller has

sizes_available_arr = list(map(int, input().split()))  # taking input of available sizes in one go

c = int(input())  # the number of customers

size_arr = []
price_arr = []

for i in range(c):
    size, price = input().split()
    size_arr.append(int(size))
    price_arr.append(int(price))

count = 0

for i in range(0,c):
    for j in range(0,x):
        if (size_arr[i] == sizes_available_arr[j]):
            count += price_arr[i]
            del sizes_available_arr[j]
            x -= 1
            break

print(count)
