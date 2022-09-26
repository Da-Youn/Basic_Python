print("0부터 9까지 for문")
for i in range(10):
    print(i)


print("0부터 11까지 짝수 for문")
for i in range(2,11,2):
    print(i)


print("0부터 9까지 while문")
i=0
while i <10:
    print(i)
    i+=1


print("엄마에게 밥 준비가 되었는지 물어보자.")
response = "아니"
while response == "아니":
    response=input("엄마, 다됐어?")
print("먹자")


print("0부터 9까지 while문-break")
i=0
while True:
    if i>=10:
        break
    print(i)
    i+=1


print("0부터 9까지 while문-continue")
i=0
while True:
    i+=1
    if i>=10:
        break
    if i%2 == 1:
        continue
    print(i)
    
