"""tuple
1.list type과 유사
2. 읽기전용( 수정 삭제 불가)
3. 기능이 적기 때문에 처리속도가 빠르다"""
tuple1: tuple = ("one", "two", "three")
#readonly기 때문에 수정 삭제 불가!
result1=tuple1[0]
result2=tuple1[1]
result3=tuple1[2]

#방1개짜리 tuple type만들시에는 주의
tuple2 = ("kmk")
#괄호 없는 튜플 생성
tuple3 = 10, 20,30

#tuple에 저장된 값을 여러 변수에 나누어 담기
a, b, c= tuple3
#두 변수에 있는 값을 서로 바꿀려면
first = "girl"
second = "boy"
# tmp=first
# first=second
# second=tmp
#위의 3줄 아래와 같이 해결 가능
first, second = second, first
print("종료")
