x,y = input().split()

k = int(y)

polynomial = input()

for i in polynomial:
    replace_x = polynomial.replace('x',x)

result = eval(replace_x) # evaluate the expression

if(result==k):
    print("True")
else:
    print("False")
