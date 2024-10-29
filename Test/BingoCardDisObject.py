import tkinter as tk
import hashlib
import random
import tkinter.messagebox as tkmg
from functools import partial


def create_widgets():#GUI部分
    generation_btn = tk.Button(root, text="ビンゴカードの生成",command = card_window)
    generation_btn.place(relx=0.5,y=50,anchor=tk.CENTER)

def card_window():
    card_number_lottery()
    card_win = tk.Toplevel()
    card_win.geometry("400x400")
    card_win.title('bingocard')
    
    card_win.rowconfigure(1, weight=1)
    card_win.columnconfigure(1, weight=1)

    title_label = tk.Label(card_win,text="ビンゴカード")
    title_label.place(relx=0.5,y=20,anchor=tk.CENTER)
#todo:btnの配置
    btn_block = tk.LabelFrame(card_win,padx=10,pady=10)
    btn_block.place(relx=0.5,y=150,anchor=tk.CENTER)
    for i in range (0,5):
        for j in range (0,5):
            list_element = 5*(i)+(j)
            number = card[list_element]
            button_text = tk.StringVar()
            button_text.set(number)
            button = tk.Button(card_win,textvariable=button_text,
                               command = partial(button_click_1,list_element),
                               width=2)
            button.bind("<1>",callback,"+")
            button.grid(in_ =btn_block,row = j,column=i)
#            button.config(command = callback(btn=button,i=list_element))

#def button_text_set():
#    for i in range (0,5):
#        for j in range (0,5):
#            list_element = 5*(i)+(j)
#            button_text.set(card[list_element])
def callback(event):
#    def nothing():
#        btn.config(bg="#008000")
#    print(f"{i}番目のボタンが押されました")
#    block_element[i] = 1
#    print(block_element)
#    return nothing
#    print(event)
#    print(i)
    # ボタンの背景色がデフォルト値だったら赤に変更し、
    if event.widget["bg"] == "SystemButtonFace":
        event.widget["bg"] = "red"
        event.widget["state"] = "disable"
#        print(f"{i}番目のボタンが押されました")
#        block_element[i] = 1
#        print(block_element)
    # 赤色になっていたら、元に戻す。
#        event.widget["bg"] = "SystemButtonFace"
#    reach_judgment(event)

    

def button_click_1(i):
    print(f"{i}番目のボタンが押されました")
    block_element[i] = 1
    print(block_element)
#         
def card_number_lottery ():
    card.clear()
    for j in range (1,26):
        card.append (card_drawing (j))
    hush_number_kari = hushing()
    hush_list.append (hush_number_kari)
    print(card)

def card_drawing (i):
    if not i == 13:#真ん中の数字用の分岐
        if i >=1 and i <=5:
            a = 1
            b = 15
        elif i >= 6 and i <= 10:
            a = 16
            b = 30
        elif i >= 11 and i <=15:
            a = 31
            b = 45
        elif i >=16 and i <= 20:
            a = 46
            b = 60
        else:
            a = 61
            b = 75
        kari = random.randint(a,b)
        while True:
            if not kari in card:
                break
            else:
                kari = random.randint(a,b)
        return kari
    else:
        return 0#0は抽選外
    
def reach_judgment(event):
    judgment_list=[]
    a=0
    for i in range (0,5):
        for j in range (0,5):
            grid_number = 5*i+j
        if event.widget["bg"] == "red":
            a += 1
        else:
            a -= 0
            
        judgment_list.append()

    #リスト内の数字のstr化
def conbo_number ():
    str_card = str(card)
    return str_card.encode('utf-8')

def hushing ():
    return hashlib.sha256(conbo_number()).hexdigest()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('This is the root window')
    root.geometry("100x100")
    block_element = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    card=[]
    hush_list=[]
    create_widgets()
    root.mainloop()