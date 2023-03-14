from tkinter import *
root = Tk()

def search():
    return 2


message_label = Label(text='enter word',
                      font=('Arial', 16))

output_label = Label(font=('Arial', 16))

entry = Entry(font=('Arial', 16), width=10)

calc_button = Button(text='Ok',
                     font=('Arial', 16),
                     command = search())
message_label.grid(row=0, column=0,)

result_label =  Label(text = 'hello world',
                      font = ('Arial', 16))

entry.grid(row=0, column = 1)

calc_button.grid(row=0, column = 2)

##output_label.grid(row=1, column=0, columnspan=3)

word = entry.get()


result_label.grid(row=1, column = 0)


mainloop()
