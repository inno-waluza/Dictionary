from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def search():
    try:
    
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"

    except Exception as e:
        #error messege
        messagebox.showerror("Error, Word not found or no internet connection!")

def display():
    return 3

message_label = Label(text='enter word',
                      font=('Arial', 16))

output_label = Label(font=('Arial', 16))

entry = Entry(font=('Arial', 16), width=10)

search_button = Button(text='Search',
                     font=('Arial', 16),
                     command = search())
message_label.grid(row=0, column=0,)

result_label =  Label(text = 'meaning will be here',
                      font = ('Arial', 16))

entry.grid(row=0, column = 1)

search_button.grid(row=0, column = 2)

##output_label.grid(row=1, column=0, columnspan=3)

word = entry.get()


result_label.grid(row=1, column = 0)


mainloop()
