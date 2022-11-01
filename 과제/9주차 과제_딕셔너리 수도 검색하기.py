
#나라별 수도 사전 

c_dict={'대한민국':'서울',
            '일본':'도쿄',
            '미국':'워싱턴D.C',
            '태국':'방콕',
            '독일':'베를린'
            }

def dic(country):
    if country in c_dict:
        print(c_dict[country])
    else:
        answer=input("사전에 없는 단어입니다.추가할까요?[y/n]")
        if answer=="y":
            capital=input("해당하는 나라의 수도를 입력해 주세요:")
            c_dict[country]=capital
            print("사전에 추가되었습니다.")
        print(c_dict)

while True:
    country=input("검색할 나라의 이름을 입력하세요[종료 시 q입력]:")
    if country == "q":
        break
    dic(country)
    


