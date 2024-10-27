import tkinter as tk
import hashlib
import numpy as np
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
        self.block_element = np.zeros((5,5))
        print(self.block_element)
        self.pack_propagate(0)
        self.create_number()

    def create_number(self):
        text=tk.Label(self,text="2nd window")
        text.place(relx=0.5,y=20,anchor=tk.CENTER)
        btn_block = tk.LabelFrame(self,padx=10,pady=10)
        btn_block.place(relx=0.5,y=150,anchor=tk.CENTER)
        """
        self.button0 = tk.Button(self,text=self.card_number[0],command = lambda:self.button_click_1(0),width=2)
        self.button0.grid(in_ =btn_block,row = 0,column=0)
        self.button1 = tk.Button(self,text=self.card_number[1],command = lambda:self.button_click_1(1),width=2)
        self.button1.grid(in_ =btn_block,row = 1,column=0)
        self.button2 = tk.Button(self,text=self.card_number[2],command = lambda:self.button_click_1(2),width=2)
        self.button2.grid(in_ =btn_block,row = 2,column=0)
        self.button3 = tk.Button(self,text=self.card_number[3],command = lambda:self.button_click_1(3),width=2)
        self.button3.grid(in_ =btn_block,row = 3,column=0)
        self.button4 = tk.Button(self,text=self.card_number[4],command = lambda:self.button_click_1(4),width=2)
        self.button4.grid(in_ =btn_block,row = 4,column=0)
        self.button5 = tk.Button(self,text=self.card_number[5],command = lambda:self.button_click_1(5),width=2)
        self.button5.grid(in_ =btn_block,row = 0,column=1)
        self.button6 = tk.Button(self,text=self.card_number[6],command = lambda:self.button_click_1(6),width=2)
        self.button6.grid(in_ =btn_block,row = 1,column=1)
        self.button7 = tk.Button(self,text=self.card_number[7],command = lambda:self.button_click_1(7),width=2)
        self.button7.grid(in_ =btn_block,row = 2,column=1)
        self.button8 = tk.Button(self,text=self.card_number[8],command = lambda:self.button_click_1(8),width=2)
        self.button8.grid(in_ =btn_block,row = 3,column=1)
        self.button9 = tk.Button(self,text=self.card_number[9],command = lambda:self.button_click_1(9),width=2)
        self.button9.grid(in_ =btn_block,row = 4,column=1)
        self.button10 = tk.Button(self,text=self.card_number[10],command = lambda:self.button_click_1(10),width=2)
        self.button10.grid(in_ =btn_block,row = 0,column=2)
        self.button11 = tk.Button(self,text=self.card_number[11],command = lambda:self.button_click_1(11),width=2)
        self.button11.grid(in_ =btn_block,row = 1,column=2)
        self.button12 = tk.Button(self,text=self.card_number[12],command = lambda:self.button_click_1(12),width=2)
        self.button12.grid(in_ =btn_block,row = 2,column=2)
        self.button13 = tk.Button(self,text=self.card_number[13],command = lambda:self.button_click_1(13),width=2)
        self.button13.grid(in_ =btn_block,row = 3,column=2)
        self.button14 = tk.Button(self,text=self.card_number[14],command = lambda:self.button_click_1(14),width=2)
        self.button14.grid(in_ =btn_block,row = 4,column=2)
        self.button15 = tk.Button(self,text=self.card_number[15],command = lambda:self.button_click_1(15),width=2)
        self.button15.grid(in_ =btn_block,row = 0,column=3)
        self.button16 = tk.Button(self,text=self.card_number[16],command = lambda:self.button_click_1(16),width=2)
        self.button16.grid(in_ =btn_block,row = 1,column=3)
        self.button17 = tk.Button(self,text=self.card_number[17],command = lambda:self.button_click_1(17),width=2)
        self.button17.grid(in_ =btn_block,row = 2,column=3)
        self.button18 = tk.Button(self,text=self.card_number[18],command = lambda:self.button_click_1(18),width=2)
        self.button18.grid(in_ =btn_block,row = 3,column=3)
        self.button19 = tk.Button(self,text=self.card_number[19],command = lambda:self.button_click_1(19),width=2)
        self.button19.grid(in_ =btn_block,row = 4,column=3)
        self.button20 = tk.Button(self,text=self.card_number[20],command = lambda:self.button_click_1(20),width=2)
        self.button20.grid(in_ =btn_block,row = 0,column=4)
        self.button21 = tk.Button(self,text=self.card_number[21],command = lambda:self.button_click_1(21),width=2)
        self.button21.grid(in_ =btn_block,row = 1,column=4)
        self.button22 = tk.Button(self,text=self.card_number[22],command = lambda:self.button_click_1(22),width=2)
        self.button22.grid(in_ =btn_block,row = 2,column=4)
        self.button23 = tk.Button(self,text=self.card_number[23],command = lambda:self.button_click_1(23),width=2)
        self.button23.grid(in_ =btn_block,row = 3,column=4)
        self.button24 = tk.Button(self,text=self.card_number[24],command = lambda:self.button_click_1(24),width=2)
        self.button24.grid(in_ =btn_block,row = 4,column=4)
        """

#todo:for文で配置したい
        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                self.number = self.card_number[list_element]
                self.button = tk.Button(self,text=self.number,width=2)
                self.button.grid(in_ =btn_block,row = j,column=i)
                self.button.bind("<1>",partial(self.callback,element=list_element,beside=j,vertical=i))
        
                
    def callback(self,event,element,beside,vertical):
        
        if event.widget["bg"] == "SystemButtonFace":
            event.widget["bg"] = "red"
            event.widget["state"] = "disable"
            self.block_element[beside,vertical] = 1
            print(self.block_element)
            self.reach_judgment()

    def reach_judgment(self):
        list_sum = []
        list_sum.append(np.sum(self.block_element,axis=0))
        print(list_sum)
        list_sum.append(np.sum(self.block_element,axis=1))
        print(list_sum)

#        if list_sum in 5:
#            print("Bingo!!")
#        elif list_sum in 4:
#            print("Reach!!")
#        else:
#            pass

#    def button_click_1(self,i):
#        print(f"{i}番目のボタンが押されました")
#        self.button["state"] = "disable"
#        self.block_element[i] = 1
#        print(self.block_element)

    def button_text_set(self):
        for i in range (0,5):
            for j in range (0,5):
                list_element = 5*(i)+(j)
                self.button_text.set(self.card_number[list_element])

root = tk.Tk()
root.title("Bingo Card")#title
app = Main_aplication(root=root)
app.mainloop()