import time
from tkinter import *
import pyautogui
import pyperclip
import speech_recognition
from googletrans import Translator
from keyboard import press
import keyboard

# keyboard.press_and_release('enter') = dichthuat

# tạo bẳng và tên
root = Tk()
root.geometry('900x240')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title("Dịch tiếng VN <=> EN Hahuto")

# tạo bản nhập, và bảng hiển thị
Label(root, text="Tiếng Việt", font='arial 13 bold', bg='white smoke').place(x=200, y=10)
Input_text = Text(root, font='arial 15', height=6, wrap=WORD, padx=5, pady=5, width=30)
Input_text.place(x=30, y=40)

Label(root, text="English", font='arial 13 bold', bg='white smoke').place(x=680, y=10)
Output_text = Text(root, font='arial 15', height=6, wrap=WORD, padx=5, pady=5, width=30)
Output_text.place(x=530, y=40)


def dichthuat():
    translator = Translator()
    anhviet = translator.translate(text=Input_text.get(1.0, END))
    vietanh = translator.translate(text=Input_text.get(1.0, END), scr='en', dest='vi')
    a = anhviet.src
    # print("Ngôn ngữ nhập vào là: ", b)

    if a == "en":
        Output_text.delete(1.0, END)
        Output_text.insert(END, vietanh.text)
        pyperclip.copy(vietanh.text)
        # print("Tiếng anh là: ", vietanh.text)
    else:
        Output_text.delete(1.0, END)
        Output_text.insert(END, anhviet.text)
        pyperclip.copy(anhviet.text)
        # print(" Tiếng việt là: ", anhviet.text)


# nút xóa nội dung
def xoa():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)


# nhạp liệu bằng giọng nói
def hamnghe():
    nghe = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Sen: tớ đang nghe nè")
        nghe.adjust_for_ambient_noise(mic)
        audio = nghe.record(mic, duration=4)  # chỉnh thời gian nếu bạn muốn nói lâu hoặc cho nó chạy nhanh hơn
        you = ""
    # audio = may_nghe.record(mic)
    # may_nghe.energy_thr(mic)
    # print("Sen:tớ đang suy nghĩ nha ...")
    try:
        you = nghe.recognize_google(audio, language="vi-VI")
        print("Bạn: " + you)
    except Exception as e:
        print("Sen: tới ko hiểu" + str(e))
    return you


def noidungnoi():
    Input_text.delete("1.0", END)
    Input_text.insert("1.0", hamnghe())
    return


# hàm gửi tới messenger
def gui():
    dichthuat()
    xoa()
    # băt buộc phải mở https://www.facebook.com/messages/t
    # pyautogui.click(112, 17)
    pyautogui.click(620, 740)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    return


def dan():
    pyautogui.hotkey('ctrl', 'v')
    return


trans_btn = Button(root, text='Dịch VI-EN !', font='arial 12 bold', pady=0, command=dichthuat, bg='royal blue1',
                   activebackground='sky blue')
trans_btn.place(x=380, y=40)

trans_btn1 = Button(root, text='Xóa hết', font='arial 12 bold', pady=0, command=xoa, bg='royal blue1',
                    activebackground='sky blue')
trans_btn1.place(x=380, y=80)

trans_btn2 = Button(root, text='Giọng nói', font='arial 12 bold', pady=0, command=noidungnoi, bg='royal blue1',
                    activebackground='sky blue')
trans_btn2.place(x=380, y=120)

trans_btn3 = Button(root, text='Gửi Messenger', font='arial 12 bold', pady=0, command=gui, bg='royal blue1',
                    activebackground='sky blue')
trans_btn3.place(x=380, y=160)

# nút dán
trans_btn4 = Button(root, text='Dán (past)', font='arial 12 bold', pady=0, command=dan, bg='royal blue1',
                    activebackground='sky blue')
trans_btn4.place(x=380, y=200)

root.mainloop()
