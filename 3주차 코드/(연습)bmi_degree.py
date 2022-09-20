weight = float(input("몸무게를 입력하세요 (단위: kg) : "))
height = float(input("키를 입력하세요 (단위: cm) : "))
BMI = round(weight / (height/100)**2,2)
print("당신의 몸무게는 :", weight, "키는 :", height)
if BMI < 18.5 :
    print("체질량 지수는 :", BMI, "이고 저체중입니다.")
elif BMI < 23 :
    print("체질량 지수는 :", BMI, "이고 정상입니다.")
elif BMI < 25 :
    print("체질량 지수는 :", BMI, "이고 과제중입니다.")
elif BMI < 30 :
    print("체질량 지수는 :", BMI, "이고 비만입니다.")
else :
    print("체질량 지수는 :", BMI, "이고 고도비만입니다.")

