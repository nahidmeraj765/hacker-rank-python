n = int(input())

number_list = list(map(int,input().split()))

number_list.sort()

unique_set = set(number_list)

another_list = list(unique_set)

another_list.sort()

print(another_list[-2])
