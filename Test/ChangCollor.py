import tkinter as tk
import hashlib
import random
import tkinter.messagebox as tkmg
from functools import partial

class Main_aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=300,height=400,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.card = []
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        btn=tk.Button(self,text="ウィンドウを生成",command = self.create_window)
        btn.pack()

#    def button_click_1(self,i):
#        print(f"{i}番目のボタンが押されました")
#        self.block_element[i] = 1
#        print(self.block_element)

    def create_window(self):
        self.card_number_lottery()
        current=tk.Tk()
        current.title("2nd Window")
        card_window=Card_window(root=current,card=self.card)
        card_window.mainloop()

    def card_number_lottery (self):
        self.card.clear()
        for j in range (1,26):
            self.card.append (self.card_drawing (j))
#        print(self.card)

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

class Card_window(tk.Frame):
    def __init__(self,root=None,card=None):
        super().__init__(root,width=300,height=400,
                        borderwidth=4,relief='groove')
        self.root = root
        self.card_number = card
        self.pack()
        self.block_element = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.pack_propagate(0)
        self.create_number()

    def create_number(self):
        text=tk.Label(self,text="2nd window")
        text.place(relx=0.5,y=20,anchor=tk.CENTER)
        btn_block = tk.LabelFrame(self,padx=10,pady=10)
        btn_block.place(relx=0.5,y=150,anchor=tk.CENTER)

        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                number = self.card_number[list_element]
                
                self.button = tk.Button(self,text=number,
                                   command = partial(self.button_click_1,list_element),width=2)
                self.button.grid(in_ =btn_block,row = j,column=i)
                
    def button_click_1(self,i):
        print(f"{i}番目のボタンが押されました")
        self.button["state"] = "disable"
        self.block_element[i] = 1
        print(self.block_element)

    def button_text_set(self):
        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                self.button_text.set(self.card_number[list_element])

root = tk.Tk()
root.title("Bingo Card")#title
app = Main_aplication(root=root)
app.mainloop()