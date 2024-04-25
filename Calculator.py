import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        #self.filemenu.add_command(label='close', command=self.on_closing)
        #self.filemenu.add_separator()
        self.filemenu.add_command(label='close', command='exit') # if you put command=self.on_closing, it'll do the same thing as x-ing it out

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label='Show Message', command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')

        self.root.config(menu=self.menubar) #adding menubar to the root

        self.label = tk.Label(self.root, text = 'your message', font = ('Arial', 12))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 12))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font = ('Arial', 12), variable = self.check_state)

        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 12), command = self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text='Clear', font=('Arial', 12), command = self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END ))

    def shortcut(self, event):
        if event.state == 0 and event.keysym == 'Return': #event.state is 4 when we ctrl enter
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you want to quit?'):
            messagebox.showinfo(title='No', message='No you\'re not') #self.root.destroy()
            messagebox.showinfo(title='And', message='And you never will!!')

    def clear(self):
        self.textbox.delete(1.0, tk.END)
                

MyGUI()
