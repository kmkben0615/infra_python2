# BinaryTest/gui02.py

import tkinter as tk
from tkinter import messagebox

def clicked():
    input_value = entry.get().strip() 
    #10진수 2진수로
    if not input_value:
        return 

    try:
        num = int(input_value)
        # 범위 체크: 0~255 사이가 아니면 경고창 띄우기
        if not (0 <= num <= 255):
            messagebox.showerror("에러", "0~255 사이의 숫자를 입력해 주세요!")
            return

        # 2진수 8자리 변환
        binary_result = f"{num:08b}"
        result_label.config(text=binary_result, fg="blue")
    except Exception as e:
        result_label.config(text="숫자만 입력 가능 합니다", fg="red")

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("나의 App")
    root.geometry("400x300") # 레이블이 많아져서 높이를 조금 키웠습니다.

    # 1. 안내 레이블
    # (오류 지점 수정: tk.Label(r -> tk.Label(root))
    label = tk.Label(root, text="10 진수를 2진수로 변환")
    label.pack(pady=20)

    # 2. 입력창 
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() 

    # 3. 전송 버튼 (이 부분이 빠져있었습니다)
    btn = tk.Button(root, text="전송", command=clicked)
    btn.pack(pady=10)

    # 4. 결과 표시 레이블 (이 부분이 빠져있었습니다)
    result_label = tk.Label(root, text="결과...", font=("Arial", 12, "bold"))
    result_label.pack(pady=20)

    root.mainloop()