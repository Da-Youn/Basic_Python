#BMI 계산하기
#몸무게와 키를 입력받은 후 체질량 지수 표시하기

weight=float(input("몸무게를 입력하세요: "))
height=float(input("키를 입력하세요: "))
bmi=weight/(height/100)**2
print("체질량지수는 ",round(bmi,2),"입니다")

