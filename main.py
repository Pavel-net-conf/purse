import tkinter as tk


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog  = tk.Button(toolbar,text='Добавить позиции',command=self.open_dialog,bg='#d7d8e0',bd=0,compound=tk.TOP,image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __int__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Добавить расходы\расходы')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Purse')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.mainloop()
