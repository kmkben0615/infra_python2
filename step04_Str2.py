#주소 이름 좋아하는 음식 2가지
#json, xml, yaml
#info는 str type 이긴 한데 문자열이 특별한 형식 json
import json


info = '''{
    "name":"김민규",
    "addr":"송파구",
    "foods":["돈까스","피자"]
}'''
result=json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])
#dict에 저장된 데이터를 json 문자열로 변환
result2 = json.dumps(result)
print("종료됨")
