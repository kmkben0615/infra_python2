#dict type에 대해 알아보자
"""
dict type
1. key:value 형ㄷ로 테이터를 저장한다
2. 슨서가 없는 데이터이다
3. key값을 이용해서 저장된 값을 참조한다.
 """
#회원 1명의 데이터
mem1 = {"num" : 1, "name":"kmk", "isMan":True}
#info1 = [1,"kmk",True]
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])
#dict 안에 내용을 참조해서 변수에 담기
a=mem1["num"]
b=mem1["name"]
c=mem1["isMan"]
#dect안의 내용을 수정하기
#mem1=mem1["num"]=23
mem1=mem1["name"]="kmk"
mem1=mem1["issMan"]=False
#모든값삭제
mem1.clear()