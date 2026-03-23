#BinaryTest/test01.py
#phython에서 이진수 다루기

#2진수는 숫자를 만들때 prefix로 0b
num1 = 0b1010
result=num1+10
print(result)


num2 = 150
result2:str = bin(num2)#bin() 함수 호출하면서 10진수를 넣어주면 2짘ㄴ수 숫자 값이 나온다.
print(result2)

print('----------------------------------------')
line="abcde1234"
print(line[5:10])#5번 인덱스 이상 10인덱스 미만 문자열

#위의 result2 문자열에서 (obxxxxx)에서 0b를 제거한 순수 2진수 형태의 문자열만 얻어낼려면?
print(result2[2:])