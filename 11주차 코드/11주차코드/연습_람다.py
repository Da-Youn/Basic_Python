#def check_score(x):
#    if x>=80:
#        return "pass"
#    else:
#        return "fail"
#print(check_score(85))

# => 더 간단하게 작성하는 방법, 람다!

check_score = lambda x: "pass" if x>=80 else "fail"
check_score(85)
