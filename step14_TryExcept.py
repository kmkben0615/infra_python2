#step14_ExceptTry.py
#main으로 실행했을때(현재파일에서 run했을떄) 실행할 code블럭 
if __name__ == "__main__":

    try:   
        #문자열
        num1_str: str = input("젯수 입력:")
        num2_str: str = input("피젯수 입력:")
         #입력한 문자열을 숫자로 변환
        num1=int(num1_str)
        num2=int(num2_str)
        result = num2/num1

        #결과 출력
        print(f"{num2}를 {num1}으로 나눈 결과 : {result}")

    except ValueError as ve:
        print(ve)
        print("숫자 형식으로 입력해주세요 ")
    except ZeroDivisionError as zde:
        print(zde)
        print("어떤 수를 0으로 나눌수는 없습니다")
     
    #어떤 중요한 마무리 작업을 합니다
    print("중요한 마무리 작업을 합니다")