a = int(input("첫번째 숫자를 입력하세요. : "))
b = int(input("두번째 숫자를 입력하세요. : "))
c = a/b
print(a,"/",b,"=",round(c,2),"입니다.")
print(str(a) + " / " + str(b) + " = " + str(round(c,2)) + " 입니다.")
print("%d / %d = %.2f 입니다." %(a,b,c))
print("{} / {} = {:.2f} 입니다." .format(a,b,c))
print("{} / {} = {} 입니다." .format(a,b,round(c,2)))
