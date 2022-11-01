a=('a','b','c')
print(a)

p={'홍길동':'010-1234-5678','강감찬':'010-1234-5679','이순신':'010-1234-5670'}

print(p.keys())

print(p.values())

print(p['홍길동'])

for name, p_no in p.items():
    if '010-1234-5679' == p_no:
        print(name)
