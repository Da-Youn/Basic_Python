temp = int(input("현재 온도는? : "))
walk = int(input("오늘 걷는 시간은? : "))
if temp >= 20 :
    if walk >= 30 :
        print("매쉬 운동화 추천")    
    else :
        print("샌들 추천")               
    print("반바지 추천")    
else :
    print("긴바지 추천")
    if walk >=30 :
        print("운동화 추천")    
    else :
        print("부츠 추천")  
