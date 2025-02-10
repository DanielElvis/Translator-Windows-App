from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import deep_translator
import langs
import requests


# Settings

root = Tk()
root.title("Translator")  
color = "gray20"
root.configure(bg=color)
root.resizable(width=False, height=False)
root.geometry("600x500")



# Function


def get_select_lang():
    selected_lang = user_text_to_lang.get()
    return selected_lang


def clear_button_func():
    result_text.delete(index1="1.0" , index2=END)


def copy_button_func():
    root.clipboard_clear()
    root.clipboard_append(result_text.get(index1="1.0" , index2=END))
    return messagebox.showinfo("Success" , "Your text was successfully copied.")


def Translator():

    try:
        if len(get_select_lang()) == 0:
            return messagebox.showerror(title="Select Language Error" , message="Please Select a Language")

        elif len(get_user_text.get()) == 0:
            return messagebox.showerror(title="Length Error" , message="cannot Translate 0 Character")     

        else:       
            translate = deep_translator.GoogleTranslator(target=get_select_lang()).translate(get_user_text.get())
                
            if len(result_text.get(index1="1.0" , index2=END)) != 0:
                result_text.delete(index1="1.0" , index2=END)
                result_text.insert(index=END , chars=translate)
                return messagebox.showinfo("Success" , "Done!")

            else:
                result_text.insert(index=END , chars=translate)
                return messagebox.showinfo("Success" , "Done!")
            

    # Exeption Connect To Internet
    except requests.exceptions.ConnectionError:
        return messagebox.showerror("Connection Error" , "Please Connect To Internet")
    
    # Exeption Valid Language
    except deep_translator.exceptions.LanguageNotSupportedException:
        return messagebox.showerror("Language Error" , "Please Select a Valid Language")
    
    # Exeption Unknown Error
    except Exception as e:
        return messagebox.showerror("An unknown error" , f"An unknown error : {e} ")

    

# Frame 1
first_frame = Frame(root, width=800, height=100 , bg=color)
first_frame.pack()

title = Label(first_frame, text="Translator", foreground="deepskyblue", font=("Arial", 25), bg=color)
title.pack(side=LEFT , padx=15 , pady=15)

# Frame 2
secound_frame = Frame(root, width=800, height=100 , bg=color)
secound_frame.pack()

user_text_label = Label(secound_frame, text="Your Text :", foreground="black", bg=color)
user_text_label.pack(side=LEFT , padx=15 , pady=15)

get_user_text = StringVar()
user_text = Entry(secound_frame , textvariable=get_user_text , width=50 )
user_text.pack(side=LEFT , padx=15 , pady=15)

# Frame 3
third_frame = Frame(root, width=800, height=100 , bg=color)
third_frame.pack()

user_text_label = Label(third_frame, text="To Language :", foreground="black", bg=color)
user_text_label.pack(side=LEFT , padx=15 , pady=15)

user_text_to_lang = ttk.Combobox(third_frame , values=langs.all_langs)
user_text_to_lang.pack(side=LEFT , padx=15 , pady=15)
user_text_to_lang.bind("<<ComboboxSelected>>" , get_select_lang())

# Frame 4
forth_frame = Frame(root, width=800, height=100 , bg=color)
forth_frame.pack()

user_text_label = Label(forth_frame, text="Result :", foreground="black", bg=color)
user_text_label.pack(side=LEFT , padx=15 , pady=15)

show_result = StringVar()
result_text = Text(forth_frame , font=("Arial" , 10) , height=10)
result_text.pack(side=LEFT , padx=15 , pady=15)

# Frame 5
five_frame = Frame(root, width=800, height=100 , bg=color)  # اصلاح نام
five_frame.pack(side=TOP)  # استفاده از pack در اینجا


clear_button = Button(
    five_frame,
    text = "Clear",
    bg="deepskyblue",
    width=20 , height=1,
    command=clear_button_func
)

clear_button.pack(side=LEFT , padx=15 , pady=15)


func_button = Button(
        five_frame, 
        text="Translate" , 
        bg="deepskyblue" , 
        width=20 , height=1 , 
        command=Translator
)

func_button.pack(side=LEFT , padx=15 , pady=15)


copy_button = Button(
     five_frame , 
     text="Copy To Clipboard" , 
     bg='deepskyblue',
     width=20 , height=1,
     command=copy_button_func
     )

copy_button.pack(side=LEFT , padx=15 , pady=15)
root.mainloop()





