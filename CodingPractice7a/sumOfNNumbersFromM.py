m=int(input())
n=int(input())

count = 0
res=0
while count < n:
    res = res + m
    m=m+1
    count=count +1
print(res)