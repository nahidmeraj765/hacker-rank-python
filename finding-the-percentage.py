n = int(input())

name_list = []
math_list = []
english_list = []
biology_list = []

for i in range(0,n):
    name,math,english,biology = input().split()
    name_list.append(name)
    math_list.append(float(math))
    english_list.append(float(english))
    biology_list.append(float(biology))

string = input()

for i in range(0,n):
    if(string==name_list[i]):
        avg = (math_list[i]+english_list[i]+biology_list[i])/3
        print(f"{avg:.2f}")

