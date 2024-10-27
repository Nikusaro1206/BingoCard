for i in range (0,5):
    for j in range (0,5):
        list_element = 5*(i)+(j)

        print(f"self.button{list_element} = tk.Button(self,text=self.card_number[{list_element}],command = lambda:self.button_click_1({list_element}),width=2)")
        print(f"self.button{list_element}.grid(in_ =btn_block,row = {j},column={i})")
