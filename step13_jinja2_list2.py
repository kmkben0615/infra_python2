#step13_jija2_list2.py

# #게시글 목록이 담긴 리스트
# posts:list=[{"id":1,"writer":"작성자1","title":"제목1"},
#             {"id":2,"writer":"작성자2","title":"제목2"},
#             {"id":3,"writer":"작성자3","title":"제목3"}]

# 게시글 목록이 담긴 리스트

from jinja2 import Template


posts:list = [
    {"id": 1, "writer": "작성자1", "title": "제목1"},
    {"id": 2, "writer": "작성자2", "title": "제목2"},
    {"id": 3, "writer": "작성자3", "title": "제목3"}
]
my_template: str = '''
글목록 입니다
{% for post in posts %}
- 글번호: {{ post.id }} 작성자: {{ post.writer }} 제목: {{ post.title }}
{% endfor %}
'''
temp: Template = Template(my_template)
result: str = temp.render(posts=posts)
print(result)