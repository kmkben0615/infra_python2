import tkinter as tk

# root 창 생성
root = tk.Tk()
root.title("2진수 변환기")
root.geometry("400x300")

label = tk.Label(root, text="0~255 사이의 숫자를 입력하세요")
label.pack(pady=10)

# 입력창
num_entry = tk.Entry(root, font=("Arial", 12))
num_entry.pack(pady=5)
num_entry.focus() 

# 버튼 클릭 시 실행될 함수
def clicked():
  
    val = num_entry.get()
    
    # 숫자로 바꾸기
    num = int(val)
  
    if 0 <= num <= 255:
     
        result = format(num, '08b')
        label2.config(text=f"결과: {result}")
    else:
       
        label2.config(text="0~255 사이만 입력 가능!")

#버튼
btn = tk.Button(root, text="전송", command=clicked, width=10, bg="lightgray")
btn.pack(pady=15)

label2 = tk.Label(root, text="결과...")
label2.pack(pady=20)

root.mainloop()