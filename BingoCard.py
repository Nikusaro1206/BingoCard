import tkinter as tk
import hashlib
import random

def cardDrawing (i):
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

#リスト内の数字のstr化
def conboNumber ():
    str_card = str(card)
    return str_card.encode('utf-8')


card = []
for j in range (1,26):
    card.append (cardDrawing (j))

print(card)
print(len(card))
hs = hashlib.sha256(conboNumber()).hexdigest()
print(hs)