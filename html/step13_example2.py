#step13_example2.py
from jinja2 import FileSystemLoader, Environment, Template

#템플릿 파일이 위치한 폴더 설정
file_loader=FileSystemLoader("html")

#환경객체
env = Environment(loader=file_loader)

# 템플릿 파일 로딩한 TEmplate 객체 얻어오기
temp:Template = env.get_template("index.html")

#템플릿에 랜더링할 데이터(실제로는 DB에서 읽어오게 된다)
notice_data={
    "title":"오늘의 공지사항",
    "notice": ["드디어 불금입니다", "어쩌구......", "저쩌구....."]
}
# data 를 전달해서 렌더링하기
result:str = temp.render(notice_data)


# 출력하기
print(result)
