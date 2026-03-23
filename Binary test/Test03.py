#BinaryTest/Test03.py

#비트연산 or, xor, not
a=0b1100
b=0b1010
#bit or연산
print(bin(a|b))#|=or연산자

# bit xor연산
print(bin(a^b))#다른것만 1

#bit not 연산
print(bin(~a))#-(a+1)
print(bin(~a & 0xf))