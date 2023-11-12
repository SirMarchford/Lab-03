import tkinter as tk
from tkinter import ttk
import random
import pygame

def close():
    pygame.mixer.music.stop()
    window.destroy()

def clear():
    hex_entry.delete(0, tk.END)  # Clear the Entry widget
    key_label.config(text="")   # Clear the result label

def generate_key(hex_part):
    dec_part = int(hex_part, 16)
    key = f"{dec_part // 1000:03d}-{dec_part % 1000:03d}-{random.randint(0, 999):03d} {random.randint(0, 99):02d}"
    return key

def generate_button_clicked():
    hex_part = hex_entry.get()
    key = generate_key(hex_part)
    key_label.config(text=key)


# Создаем главное окно и Устанавливаем изображение фона
window = tk.Tk()
window.title("Keygen")
window.geometry('1200x630')
bg_img = tk.PhotoImage(file='eurotruck.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

#Создаем и располагаем виджеты
hex_label = ttk.Label(frame, text="Enter HEX part:")
hex_label.grid(column=0, row=0, padx=10, pady=15)

hex_entry = ttk.Entry(frame)
hex_entry.grid(column=5, row=0, padx=10, pady=15)

lbl_roots = ttk.Label(frame, text='The Result Key is:')
lbl_roots.grid(column=0, row=3, padx=10, pady=15)

key_label = ttk.Label(frame, text="")
key_label.grid(column=5, row=3, padx=10, pady=15)

generate_button = ttk.Button(frame, text="Generate Key", command=generate_button_clicked)
generate_button.grid(column=0, row=6, padx=10, pady=15)

btn_exit = ttk.Button(frame, text='Exit', command=close)
btn_exit.grid(column=5, row=6, padx=10, pady=15)

btn_clear = ttk.Button(frame, text='Clear', command=clear)
btn_clear.grid(column=3, row=6, padx=10, pady=15)

# Initialize Pygame mixer
pygame.mixer.init()
# Load and play background music
pygame.mixer.music.load('sunshine-whistle-175139.mp3')
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Запускаем главный цикл
window.mainloop()
