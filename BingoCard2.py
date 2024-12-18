import tkinter as tk
import hashlib
import numpy as np
import random
from functools import partial

class Main_aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=100,height=70,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.card = []
        self.hush_number = []
        self.pack_propagate(0)
        self.create_widgets()

    #ボタンを配置
    def create_widgets(self):
        btn=tk.Button(self,text="カードを生成",command = self.create_window)
        btn.pack()

    #カード用クラスの実行
    def create_window(self):
        new_hush = self.hush_jedgment()#カード番号の抽選とハッシュ値の取得
        #check:抽選とハッシュ値は別にしたほうがいいかも追いかけづらい
        self.hush_number.append(new_hush)
        current=tk.Tk()
        current.title(f"BINGO CARD")
        card_window=Card_window(root=current,card=self.card,hush = new_hush)
        card_window.mainloop()

    #カード番号の抽選とハッシュ値の取得
    def hush_jedgment(self):
        self.card = self.card_number_lottery()#カード番号の抽選
        while True:#重複回避
            new_hush_number = self.hushing()
            if new_hush_number in  self.hush_number:
                self.card = self.card_number_lottery()#カード番号の再抽選
            else:
                break
        return new_hush_number
    
    #カード番号の抽選
    def card_number_lottery (self):
        card = []
        for column in range (1,26):
            card.append(self.card_drawing (column,card))#カード番号の抽選２
        return card
    
    #カード番号の抽選２
    def card_drawing (self,i,card):
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
        
    #ハッシュ値の取得
    def hushing (self):
        str_card = str(self.card)
        return hashlib.md5(str_card.encode('utf-8')).hexdigest()

class Card_window(tk.Frame):
    def __init__(self,root=None,card=None,hush=None):
        super().__init__(root,width=400,height=600,
                        borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.block_element = np.zeros((5,5))#5x5の配列0詰め
        self.pack_propagate(0)
        self.create_number(card,hush)

    def create_number(self,card_number,hush):
        text=tk.Label(self,text=f"ハッシュ値:{hush}")
        text.place(relx=0.5,y=580,anchor=tk.CENTER)
        decorasion_sp = tk.LabelFrame(self,padx=10,pady=10,relief="flat")
        decorasion_sp.place(relx=0.5,y=80,anchor=tk.CENTER)
        BINGO = ["B","I","N","G","O"]
        for i in range (0,5):
            decorasion = BINGO[i]
            decorasion_label = tk.Label(self,text = decorasion,font=("Times",27,"bold"),width=3)
            decorasion_label.grid(in_ = decorasion_sp,row=0,column=i)

        btn_block = tk.LabelFrame(self,padx=10,pady=10)
        btn_block.place(relx=0.5,y=300,anchor=tk.CENTER)
        #for文でbuttonウィジェット配置
        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                number = card_number[list_element]
                button = tk.Button(self,text=number,font=("Times",25,"bold"),width=3)
                button.grid(in_ =btn_block,row = j,column=i)
                button.bind("<1>",partial(self.callback,beside=j,vertical=i))

        jedgement_sp = tk.LabelFrame(self,text="判定",padx=10,pady=10)
        reach_sp = tk.Label(self,text="REACH:",width=7)
        self.reach_label = tk.Label(self,text=0,width=2)
        bingo_sp = tk.Label(self,text="BINGO:",width=7)
        self.bingo_label = tk.Label(self,text=0,width=2)

        jedgement_sp.place(relx=0.5,y=520,anchor=tk.CENTER)
        reach_sp.grid(in_=jedgement_sp,row=0,column=0)
        self.reach_label.grid(in_=jedgement_sp,row=0,column=1)
        bingo_sp.grid(in_=jedgement_sp,row=1,column=0)
        self.bingo_label.grid(in_=jedgement_sp,row=1,column=1)

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
        for i in range (0,6):#check:配列結合して分岐を1セットにするのもありかも
            if list_sum_vartical_all[i] == 5:
                bingo_count += 1
            elif list_sum_vartical_all[i] == 4:
                reach_count += 1
            else:
                pass
            if list_sum_beside_all[i] == 5:
                bingo_count += 1
            elif list_sum_beside_all[i] == 4:
                reach_count += 1
            else:
                pass
        self.reach_label.config(text=reach_count)#2つ目のクラスだと.setは使えない
        self.bingo_label.config(text=bingo_count)

    #斜め用判定
    def cros_sum(self,sum_type):
        a = 0
        if sum_type == 0:#右ななめsum_type=0
            for i in range (0,5):
                a += self.block_element[i,i]
        if sum_type == 1:#左ななめsum_type=1
            for i in range (0,5):
                a += self.block_element[i,4-i]
        return a
    
root = tk.Tk()
root.title("Bingo Card")#title
app = Main_aplication(root=root)
app.mainloop()