#step09.
'''비번을 입력 받아서 입력한 비밀번호가 8자리 이상이면 사용 가능한 비말번호입이가. 그허지 않으면 사용불가 입니다
'''
input_ps=input("비번 입력")
if len(input_ps) >=8:
    print("사용가능")
else:
    print("사용불가")