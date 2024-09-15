t = int(input())

for i in range(1,t+1):
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    n = int(input())
    if(n==50):
        print(count_a)
    elif(n==0):
        while(n!=50):
            n = n + 2
            count_b = count_b + 1
        print(count_b)
    elif(n>50):
        while(n!=50):
            if(n>50):
                n = n - 3
                count_c = count_c + 1
            elif(n<50):
                n = n + 2
                count_c = count_c + 1
        print(count_c)
    elif(n<50):
        while(n!=50):
            if(n<50):
                n = n + 2
                count_d = count_d + 1
            elif(n>50):
                n = n - 3
                count_d = count_d + 1
        print(count_d)

