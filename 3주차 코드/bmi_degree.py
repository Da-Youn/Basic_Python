weight=float(input("몸무게를 입력하세요: "))
height=float(input("키를 입력하세요: "))
bmi=round(weight/(height/100)**2,2)
if bmi<18.5:
    print("체질량지수는 ",bmi,"이고 저체중입니다")      
elif bmi<23:
    print("체질량지수는 ",bmi,"이고 정상입니다")     
elif bmi<25:
    print("체질량지수는 ",bmi,"이고 과체중입니다")     
elif bmi<30:
    print("체질량지수는 ",bmi,"이고 비만입니다")     
else:
    print("체질량지수는 ",bmi,"이고 고도비만입니다")     

    

