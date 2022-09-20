# 년도를 입력하면 윤년과 평년을 판단해주는 코드입니다.

year=int(input("년도를 입력하세요 : "))
if (year %4==0 and year%100 !=0 ) or year%400 ==0:
    print(year,"년도는 윤년입니다")
else:
    print(year,"년도는 평년입니다")

