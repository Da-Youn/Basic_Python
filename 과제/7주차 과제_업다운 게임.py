import random

answer = random.randint(1,100)
cnt = 0
            
while True:
    guess = int(input("값을 입력하세요:"))
    cnt+=1
    if answer == guess:
        print("정답: 맞았어요.",cnt,"번만에 맞췄네요.")
        break
    elif answer < guess:
        print("down")
        
        continue
    else:
        print("up")
        continue
    
