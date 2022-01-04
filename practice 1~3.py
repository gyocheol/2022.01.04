# 1번 문제
f = open('yesterday.txt','r')
lines = f.readlines()
f.close()
words = []
for line in lines:
    for w in line.split():
        words.append(w.lower())
list = list(set(words))
list.sort()
d = dict()
for w in list:
    d[w] = words.count(w)
for w in d.items():
    print(w)

# 2번 문제
def sum(list_num,list_sum):
    with open('list_num.txt','r') as r:
        lines = r.readlines()
    print(lines)
        with open('list_sum.txt', 'w') as w:
            for line in lines:
                a,b = map(int, lines.split())
                w.write(f'{a} + {b} + {a+b}')

# 3번 문제
def input_member(infile):
    with open(infile, 'w', encoding='utf-8') as f:
        while True:
            member = input('멤버를 입력하세요.(종료는 q) : ')
            if member == 'q':
                break
            else:
                f.write(member+'\n')

def output_member(outfile):
    with open(outfile, 'r', encoding='utf-8') as f:
        print(f.read())

while True:
    opt = input("저장 1, 출력 2 종료 q : ")
    if opt == '1':
        infile = input('멤버명단을 저장한 파일명을 입력하세요 : ')
        input_member(infile)
    elif opt == '2':
        outfile = input('멤버명단을 저장된 파일명을 입력하세요 : ')
        output_member(outfile)
    elif opt == 'q':
        break
    else:
        print('잘못입력하셨습니다.')