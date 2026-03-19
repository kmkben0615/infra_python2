#yaml 형식의 문자열 다루기

#yaml 문자열을 다룰떄는 외부 모듈을 pip로 설치를 해서 import를 해야함
info='''
name: 김민규
addr: 송파구
foods:
  -돈까스              #yaml형식임
  -피자
isMan: true
body:
  weight: 85
  height: 179
'''
#검색 혹은  ai의 도움을 받아서 info에 들어있는 문자열을 dict type으로 바꾸세여
#그런 다음 dict에 들어있는 내용을 확인후 다시 dict에 있는 내용을 이해해서 yaml 문자열 형식으로 변환해보세요
import yaml

# 1. 주어진 문자열 정의
info = '''
name: 김민규
addr: 송파구
foods:
  - 돈까스
  - 피자
isMan: true
body:
  weight: 85
  height: 179
'''

# yaml형식의 문자열을 dict 타입으로 변환 (yaml.safe_load 사용)
info_dict = yaml.safe_load(info)


print(info_dict)
print("----------------------------------------------------------------------------")
# 3. dict 데이터를 다시 YAML 문자열 형식으로 변환 (yaml.dump 사용)
# allow_unicode=True는 한글이 깨지지 않게 해줍니다.
yaml_output = yaml.dump(info_dict, allow_unicode=True, sort_keys=False)

print("--- 다시 변환된 YAML 문자열 ---")
print(yaml_output)