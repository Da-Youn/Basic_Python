friends = ['가연','나연','다연','사연', '아연','하연']
while True:
    name = input("찾고싶은 친구의 이름을 입력하세요(종료를 원할 시 '검색종료' 입력): ")
    if name == "검색종료":
        break
    elif name in friends:
        print(friends.index(name),name)
        continue
    else:
        print(name,"은 명단에 없네요...")
        name_add = input("추가하시겠습니까? [예/아니오]: ")
        if name_add == "예":
            friends.append(name)
            friends.sort()
            print(friends)
        elif name_add == "아니오":
            continue
print("검색을 종료합니다.")    

   
