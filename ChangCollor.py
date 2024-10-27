import tkinter as tk

def setnumber():
    column = -1
    row = 0
    root = tk.Tk()
    root.title('numbers')
    root.geometry('470x310')
    for i in range(101):
        if i > 0:
            if i%10 == 1:
                row += 1 
                column = -1
            column += 1
            text=f'{i}'
            btn = tk.Button(root, text=text)
            btn.grid(column=column, row=row)
            btn.config(command=collback(btn))
    root.mainloop()

def collback(btn):
    def nothing():
        btn.config(bg='#008000')
    return nothing