import tkinter as tk
import hashlib
import random
import tkinter.messagebox as tkmg

class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=300,height=400,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.card = []
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):#GUI部分
        generation_btn = tk.Button(self, text="ビンゴカードの生成",command = self.create_window)
        generation_btn.pack()

    def create_window(self):
        self.card_number_lottery()
        self.window2 = tk.Toplevel(self)
        self.window2.focus_set()
        self.window2.geometry("200x200")
        self.create_widgets2()

    def create_widgets2(self):
        title_label = tk.Label(self.window2,text="ビンゴカード")
        title_label.pack()
#todo:btnの配置
#         
    def card_number_lottery (self):
        for j in range (1,26):
            self.card.append (self.card_drawing (j))

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