from jinja2 import Template
my_template="""
    번호:{{num}}
    이름:{{name}}
    주소:{{addr}}
"""
#template에 출력할 데이터 준비
mem1 = {"num":1, "name": "김구라", "addr": "노량진"}#dict type
mem2 = {"num":2, "name": "김구", "addr": "송파구"}
#import한 Template 클래스의 생성자에 my_template 문자열을 넣어서 객체를 생성한다.
temp: Template = Template(my_template)
result1=temp.render(mem1)
print(result1)
result2=temp.render(mem2)
print(result2)