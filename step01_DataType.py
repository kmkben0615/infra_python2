#한줄 주석
"""sdfsdfsdfsdf
"""
print("stenum")
num1=10
num2=15.2
name="kmk"
yourname="mmm"
#순서기 중요한 
#하나의 변수에 여러가지
foods=["닭발", "삽겹살"," 돈까스"]#list type
#        0       1        2
print(foods)
print(foods[0])
#순서 중요x 여러개의 데이터를 관리하고 싶다면...
#회원 1명의 정보
num=1
name="김구라"
addr="노량진"

mem1= {"num" :1, "name" : "김구라", "addr" : "노량진"} #dict type
#{"key": value(값)-, "key2" : ,value2...}
#dict type 만드는 방법

print(mem1)
#순서 중요x 하나의 묶음으로 관리하고 싶디면(키값없이)
mySet = {"빨강사탕", "초록사탕", "노랑사탕"}#set type
print(mySet)
#특정 코드 블럭을 필요한 시점에 일괄 실행하고 싶다면?
#함수 만드는 방법
def store():
    print("acs")
    print("dfdf")
    print("ewrewr")
#함수 실행 방법
# 함수명() 필요한 시점에 실행 
print(mem1)
store()
print(mySet)
#어떤 변수를 빈 상태로 만들고 값을 나중에ㅡ 넣고 싶다명~(None)
a = None
print("어떤 작업을 하고")
print("필요할떄 값을 넢는다")
a= "test"
#참과 거짓을 나타내는 data type (Bool)
isMan=True
isWoman=False
isDifferent=True
isRun=False