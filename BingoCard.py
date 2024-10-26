import tkinter as tk
import hashlib
import random
import tkinter.messagebox as tkmg
from functools import partial

class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=300,height=400,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.card = []
        self.pack_propagate(0)
        self.card_number_lottery(0)
        self.create_widgets()
        

    def create_widgets(self):#GUI部分

        generation_btn = tk.Button(self, text="ビンゴカードの生成",command = lambda:self.card_number_lottery(1))
        generation_btn.place(relx=0.1,y=300)

    #def create_window(self):
        #self.card_number_lottery()
        #self.window2 = tk.Toplevel(self)
        #self.window2.focus_set()
        #self.window2.geometry("200x200")
        #self.create_widgets2()

    #def create_widgets2(self):
        title_label = tk.Label(self,text="ビンゴカード")
        title_label.place(relx=0.5,y=20,anchor=tk.CENTER)
#todo:btnの配置
        btn_block = tk.LabelFrame(self,padx=10,pady=10)
        btn_block.place(relx=0.5,y=150,anchor=tk.CENTER)
        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                number = self.card[list_element]
                self.button_text = tk.StringVar()
                self.button_text.set(number)
                button = tk.Button(self,textvariable=self.button_text,
                                   command = partial(self.button_click_1,list_element),width=2)
                button.grid(in_ =btn_block,row = j,column=i)

    def button_text_set(self):
        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                self.button_text.set(self.card[list_element])

    def button_click_1(self,i):
        print(f"{i}番目のボタンが押されました")
#         
    def card_number_lottery (self,repeat):
        self.card.clear()
        for j in range (1,26):
            self.card.append (self.card_drawing (j))
        print(self.card)
        if not repeat == 0:
            self.button_text_set()
        else:
            pass

    def card_drawing (self,i):
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
                if not kari in self.card:
                    break
                else:
                    kari = random.randint(a,b)
            return kari
        else:
            return 0#0は抽選外

    #リスト内の数字のstr化
    def conbo_number (self):
        str_card = str(self.card)
        return str_card.encode('utf-8')

    def hushing (self):
        return hashlib.sha256(self.conbo_number()).hexdigest()
#todo:リーチのプログラム

root = tk.Tk()
root.title("Bingo Card")#title
app = Aplication(root=root)
app.mainloop()