class Button():
    def __init__(self, title_text, x_num, y_num):
        self.title_text = title_text
        self.x_num = x_num
        self.y_num = y_num
        self.appearance = True
        
        
        
    def hide(self):
        self.appearance = False
        
        
    def show(self):
        self.appearance = True
        
    def print_status(self):
        print("Дані про віджет:")
        print(self.title_text,self.x_num,self.y_num,self.appearance)
        
        
ok_button = Button("OK",100,100)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()
        