#step13_example.py
from jinja2 import Template
info:dict = {
        "num":1,
        "name":"김구라",
        "body":{"height":180, "weight":80},
        "hobby" : ["피아노","당구","프로그래밍"]

}
"""
위의 info안에 들어있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력해보세여
"""
my_template: str = '''
    번호: {{ num }}
    이름: {{ name }}
    키: {{ body.height }} cm
    몸무게: {{ body.weight }} kg
    취미 : {% for item in hobby %} 
            -{{item}}
         {% endfor %}
     '''
temp = Template(my_template)
result = temp.render(info)

# 4. 결과 확인
print(result)