phone_book={ '홍길동' :'1234-1111', '강감찬' : '1111-3333' }
print(phone_book)
phone_book['이순신']='111-4444'  	#추가
print(phone_book)
phone_book['홍길동']='111-2222'            #수정
print(phone_book)

del phone_book['강감찬']                         #삭제
print(phone_book.keys())   	
		 # phone_book 에 있는 모든 Key를 인쇄
print(phone_book.values())		 # phone_book 에 있는 모든 값들을 인쇄
print(phone_book['홍길동'])	  # key로 접근 가능
#print(phone_book[0] ) 	# error: 순서가 없기 때문에 				           index로는 접근할 수 없음
for name,p_no in phone_book.items(): # value로 key 찾기
    if  '111-2222'==p_no:
        print(name)
