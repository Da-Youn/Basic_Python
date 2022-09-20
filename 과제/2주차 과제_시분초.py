time = int(input("계산할 초를 입력하세요 : "))
hour = (time // 60) * 60)
minute = (time // 60) % 60
second = time % 60
print(time,"초를 계산하면",hour,"시간",minute,"분",second,"초 입니다.")
