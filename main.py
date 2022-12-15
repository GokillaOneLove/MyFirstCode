from tkinter import *
#настройка окна
root = Tk()
root.title("Калькулятор")
root.configure(bg='darkgray')
w = 400
h = 400
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#букавы и их место
label = Label(text="Сумма кредита:")
label.place(x=15, y=15)
entry = Entry()
entry.place(x=15, y=45, width=100, height=25)
label1 = Label(text="Количество месяцев:")
label1.place(x=15, y=80)
entry1 = Entry()
entry1.place(x=15, y=110, width=100, height=25)
#тело
def button_click():
    entry2.delete(0, END)
    kredit = float(entry.get())
    moun = float(entry1.get())
    moun = round(moun)
    proc = kredit / 100 * 18
    proc = float(proc)
    kp = kredit + proc
    u = kp / moun
    kp = round(kp, 2)
    u = round(u, 2)
    entry2.insert(END, kp)
    entry3.insert(END, u)
    try:
        with open('information.txt', 'w') as file:
            file.write("Сумма кредита:")
            file.write(str(kredit))
            file.write("\nКоличество месяцев:")
            file.write(str(moun))
            file.write("\nСумма кредита с процентами:")
            file.write(str(kp))
            file.write("\nЕжемесячный платеж:")
            file.write(str(u))
    except:
        print("ошибка")
#кнопка для тела
button = Button(text="Рассчитать", command=button_click)
button.place(x=15, y=150, width=145, height=35)
label2 = Label(text="Сумма кредита с процентами:")
label2.place(x=15, y=200)
entry2 = Entry()
entry2.place(x=15, y=225, width=175, height=35)
label3 = Label(text="Ежемесячный платеж:")
label3.place(x=15, y=265)
entry3 = Entry()
entry3.place(x=15, y=290, width=175, height=35)
#рут точка маин точка лууп
root.mainloop()
