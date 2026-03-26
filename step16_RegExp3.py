#Step16_RegExp3.py


import re


logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]
#logs에서 ERROR or WARN 로그인 찾아서 콘솔창에 출력
#첫 글자가 w or A or R or N인지를 검정할 수 있는 정규 표현식
pattern1=r"^{WARN}"
#[WARN]으로 시작하는지 검증할수 있는 정규 표현식
patern2=r"^\[WARN\]"
#[ERROR]로 시작하는지 검증할수 있는 정규 표현식
pattern3=r"^\[ERROR]\]"
#WARN or ERROR로 시작하는지 검증할 수 있는 정규 표현식
pattern4=r"^(WARN|ERROR)"
#[WARN] or [ERROR]로 시작하는지 검증할 수 있는 정규 표현식
pattern=r"^\[(WARN|ERROR)\]"

for tmp in logs:
    if re.search(pattern, tmp):
        print(tmp)

