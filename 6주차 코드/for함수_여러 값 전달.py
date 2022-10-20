def get_tot(start,end):
    tot = 0
    for i in range(start, end+1):
        tot += i
    return tot

t=get_tot(1,10)
print(t)

print(get_tot(1,10))

s=int(input("처음 값을 입력하세요:"))
e=int(input("마지막 값을 입력하세요:"))

print("tot:",get_tot(s,e))
