import tkinter as tk

SCard1 = []
SCard2 = []

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def Round_2():
    SCard1.append(r1f1.get())
    SCard2.append(r1f2.get())
    label_SCard1.config(text=repr(SCard1))
    label_SCard2.config(text=repr(SCard2))

    tk.Label(master, text='Round 2').grid(row=10, column=0)
    label_SCard1.grid(row=11, column=0)
    label_SCard2.grid(row=13, column=0)
    tk.Label(master, text=e1.get()).grid(row=12, column=1)
    tk.Label(master, text=e2.get()).grid(row=14, column=1)

    r2f1 = tk.Entry(master)
    r2f2 = tk.Entry(master)

    r2f1.grid(row=12, column=2)
    r2f2.grid(row=14, column=2)

    quit_button_2 = tk.Button(master, text='Quit', command=master.quit)
    quit_button_2.grid(row=15, column=0, sticky=tk.W, pady=4)
    
    continue_button_2 = tk.Button(master, text='Continue', command=show_entry_fields)
    continue_button_2.grid(row=15, column=1, sticky=tk.W, pady=4)

def Round_1():
    global r1f1, r1f2, quit_button_1, continue_button_1

    tk.Label(master, text='Round 1').grid(row=5, column=0)
    tk.Label(master, text=e1.get()).grid(row=6, column=0)
    tk.Label(master, text=e2.get()).grid(row=7, column=0)

    r1f1 = tk.Entry(master)
    r1f2 = tk.Entry(master)

    r1f1.grid(row=6, column=1)
    r1f2.grid(row=7, column=1)

    quit_button_1 = tk.Button(master, text='Quit', command=master.quit)
    quit_button_1.grid(row=9, column=0, sticky=tk.W, pady=4)
    
    continue_button_1 = tk.Button(master, text='Continue', command=lambda: [Round_2(), quit_button_1.grid_remove(), continue_button_1.grid_remove()])
    continue_button_1.grid(row=9, column=1, sticky=tk.W, pady=4)

master = tk.Tk()
tk.Label(master, text="Fighter 1").grid(row=0, column=0)
tk.Label(master, text="Fighter 2").grid(row=0, column=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=0, column=3)

quit_button_main = tk.Button(master, text='Quit', command=master.quit)
quit_button_main.grid(row=3, column=0, sticky=tk.W, pady=4)

begin_button = tk.Button(master, text='Begin', command=lambda: [Round_1(), quit_button_main.grid_remove(), begin_button.grid_remove()])
begin_button.grid(row=3, column=1, sticky=tk.W, pady=4)

label_SCard1 = tk.Label(master)
label_SCard2 = tk.Label(master)

tk.mainloop()

