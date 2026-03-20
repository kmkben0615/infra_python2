#step09_if2.pu
#다증 if문 구성
#디스크 용량을 입력 받아서 90이상이면 "디스크 용량이 부족 그 외에는 정상입니다 출력"

disk=int(input("디스크 사용량을 입력(0-100)"))
if disk>=90:
    print("용량부족")
elif disk>70:
    print("확장준비")
else:
    print("정상")