
def get_tot(n):
    tot = 0
    for i in range(1,n+1):
        tot += i
    print("i=",i,"tot:",tot)

get_tot(50)



def get_tot(n):
    global i
    tot = 0
    for i in range(1,n+1):
        tot += i
    return tot

t = get_tot(50)
print(i, "까지의 합은:",t)--> ERROR

