import tkinter as tk
import hashlib
import numpy as np
import random
import tkinter.messagebox as tkmg
from functools import partial


def create_window(hush_number):
    new_hush , card = hush_jedgment(hush_number)
    hush_number.append(new_hush)
    current=tk.Tk()
    current.title(f"{new_hush}")
    card_window=Card_window(root=current,card=card)
    card_window.mainloop()

def hush_jedgment(hush_number):
    card = card_number_lottery()
    print(card)
    while True:
        new_hush_number = hushing(card)
        if new_hush_number in  hush_number:
            card = card_number_lottery()
        else:
            break
    return new_hush_number , card

def card_number_lottery ():
    card = []
    for i in range (1,26):
        card.append(card_drawing (i,card))
    return card

def card_drawing (i,card):
    if not i == 13:#真ん中の数字用の分岐
        if i >=1 and i <=5:
            a,b=1,15
        elif i <= 10:
            a , b= 16 ,30
        elif  i <=15:
            a , b= 31 ,45
        elif i <= 20:
            a , b= 46 ,60
        else:
            a , b= 61 ,75
        kari = random.randint(a,b)
        while True:
            if not kari in card:
                break
            else:
                kari = random.randint(a,b)
        return kari
    else:
        return 0#0は抽選外
    
def conbo_number (card):
    str_card = str(card)
    return str_card.encode('utf-8')

def hushing (card):
    str_card = str(card)
    return hashlib.sha256(str_card.encode('utf-8')).hexdigest()

class Card_window(tk.Frame):
    def __init__(self,root=None,card=None):
        super().__init__(root,width=400,height=600,
                        borderwidth=4,relief='groove')
        self.root = root
        self.card_number = card
        self.pack()
        self.block_element = np.zeros((5,5))
        self.pack_propagate(0)
        self.create_number()

    def create_number(self):
        text=tk.Label(self,text="Bingo Card")
        text.place(relx=0.5,y=20,anchor=tk.CENTER)
        btn_block = tk.LabelFrame(self,padx=10,pady=10)
        btn_block.place(relx=0.5,y=300,anchor=tk.CENTER)

        #for文でbuttonウィジェット配置
        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                self.number = self.card_number[list_element]
                self.button = tk.Button(self,text=self.number,font=("Times",25,"bold"),width=3)
                self.button.grid(in_ =btn_block,row = j,column=i)
                self.button.bind("<1>",partial(self.callback,beside=j,vertical=i))

        self.jedgment_window = tk.Toplevel(self)
        self.jedgment_window.title("判定結果")
        self.jedgment_window.geometry("400x600")
        jedgement_sp = tk.LabelFrame(self.jedgment_window,text="判定",padx=10,pady=10)
        reach_sp = tk.Label(self.jedgment_window,text="REACH:",width=7)
        self.reach_text = tk.StringVar()
        self.reach_text.set("0")
        reach_label = tk.Label(self.jedgment_window,textvariable=self.reach_text,width=2)
        bingo_sp = tk.Label(self.jedgment_window,text="BINGO:",width=7)
        self.bingo_text = tk.StringVar()
        self.bingo_text.set("0")
        bingo_label = tk.Label(self.jedgment_window,textvariable=self.bingo_text,width=2)

        jedgement_sp.place(relx=0.5,y=520,anchor=tk.CENTER)
        reach_sp.grid(in_=jedgement_sp,row=0,column=0)
        reach_label.grid(in_=jedgement_sp,row=0,column=1)
        bingo_sp.grid(in_=jedgement_sp,row=1,column=0)
        bingo_label.grid(in_=jedgement_sp,row=1,column=1)

    #選択されたボタンの色替え    
    def callback(self,event,beside,vertical):
        
        if event.widget["bg"] == "SystemButtonFace":#check:分岐なくてもいいかも
            event.widget["bg"] = "red"
            event.widget["state"] = "disable"
            self.block_element[beside,vertical] = 1
            self.reach_judgment()

    #リーチとビンゴの判定
    def reach_judgment(self):
        bingo_count=0
        reach_count=0
        list_sum_vartical = np.sum(self.block_element,axis=0)
        list_sum_vartical_all = np.append(list_sum_vartical
                                          ,self.cros_sum(0))#あとで繰り返し処理しやすいように右斜を縦判定に
        list_sum_beside = np.sum(self.block_element,axis=1)
        list_sum_beside_all = np.append(list_sum_beside
                                        ,self.cros_sum(1))#あとで繰り返し処理しやすいように左斜を横判定に
        
        #0-4で各方向の開いたマスのリーチ判定,5番目で斜めの判定
        for i in range (0,6):
            if list_sum_vartical_all[i] == 5:
                bingo_count += 1
            if list_sum_beside_all[i] == 5:
                bingo_count += 1
            if list_sum_vartical_all[i] == 4:
                reach_count += 1
            if list_sum_beside_all[i] == 4:
                reach_count += 1
        print(f"raach:{reach_count}")
        print(f"bingo:{bingo_count}")
        self.reach_text.set(reach_count)#check:更新指示しているのにGUIに数字が表示されない
        self.bingo_text.set(bingo_count)

    def cros_sum(self,sum_type):
        a = 0
        #右ななめsum_type=0
        if sum_type == 0:
            for i in range (0,5):
                a += self.block_element[i,i]
        #左ななめsum_type=1
        if sum_type == 1:
            for i in range (0,5):
                a += self.block_element[i,4-i]
        return a
    
hush_number = []
root = tk.Tk()
root.title("Bingo Card")#title
frm = tk.Frame(root)
btn=tk.Button(root,text="ウィンドウを生成",command = lambda:create_window(hush_number))
btn.pack()
root.mainloop()