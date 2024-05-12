from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Multilingual Translator")
root.geometry("590x420")

# Load the background image
bg_image = Image.open("backgroundimg.jpeg")
bg_image = bg_image.resize((590, 420), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg_image)

frame1 = Frame(root, width=590, height=420, relief=RIDGE, borderwidth=5)
frame1.place(x=0, y=0)

# Create a label to hold the background image
background_label = Label(frame1, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(
    root, text="Multilingual Translator", font=("Helvetica 20 bold"), fg="black"
).pack(pady=10)


def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == "":
        messagebox.showerror("Multilingual Translator", "Enter the text to translate!")
    else:
        text_entry2.delete(1.0, "end")
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert("end", output.text)


def clear():
    text_entry1.delete(1.0, "end")
    text_entry2.delete(1.0, "end")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        text_entry1.delete(1.0, END)
        text_entry1.insert(END, query)
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Could not understand audio input.")


a = tk.StringVar()
auto_select = ttk.Combobox(
    frame1, width=27, textvariable=a, state="randomly", font=("verdana", 10, "bold")
)
auto_select["values"] = ("Auto select",)
auto_select.place(x=15, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(
    frame1, width=27, textvariable=l, state="randomly", font=("verdana", 10, "bold")
)
choose_language["values"] = (
    "English",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Spanish",
    "Arabic",
    "Bulgarian",
    "Czech",
    "Hungarian",
    "Polish",
    "Romanian",
    "Russian",
    "Slovak",
    "Slovene",
    "Serbian",
    "Ukrainian",
)

choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 = Text(
    frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15)
)

text_entry1.place(x=10, y=100)

text_entry2 = Text(
    frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15)
)

text_entry2.place(x=300, y=100)

btn1 = Button(
    frame1,
    command=translate,
    text="Translate",
    relief=RAISED,
    borderwidth=2,
    font=("verdana", 10, "bold"),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
)

btn1.place(x=15, y=300)

btn2 = Button(
    frame1,
    command=clear,
    text="Clear",
    relief=RAISED,
    borderwidth=2,
    font=("verdana", 10, "bold"),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
)
btn2.place(x=210, y=300)

btn_listen = Button(
    frame1,
    text="Listen",
    command=listen,
    relief=RAISED,
    borderwidth=2,
    font=("verdana", 10, "bold"),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
)
btn_listen.place(x=315, y=300)

btn_speak = Button(
    frame1,
    text="Speak",
    command=lambda: speak(text_entry2.get("1.0", "end-1c")),
    relief=RAISED,
    borderwidth=2,
    font=("verdana", 10, "bold"),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
)
btn_speak.place(x=488, y=300)

root.mainloop()
