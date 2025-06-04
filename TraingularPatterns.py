#Lower Triangular Pattern:

n = 10
for i in range(1,n + 1):
    print('*'* i)
    
print("--"*10)

#Upper Triangular Pattern:

m=10
for i in range(m):
    for j in range(m):
        if j<i:
            print("",end="")
        else:
            print("*",end="")
    print()
    
print("--"*10)

#pyramid Pattern:

k = 10
for i in range(1, k + 1):
    print(' ' * (k - i) + '*' * (2 * i - 1))
