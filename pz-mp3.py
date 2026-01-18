import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox, filedialog
from customtkinter import FontManager
import sys
import subprocess
import os

selected_file = ""

def file():
   global selected_file
   selected_file = filedialog.askopenfilename(
      defaultextension=".txt",
      filetypes=[("Аудиофайлы", "*.mp3"), ("Аудиофайлы", "*.wav")]
)

def start():
   if not selected_file:
      messagebox.showinfo('pz-mp3', 'Файл не выбран')
      return
   
   output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Аудиофайлы", "*.mp3"), ("Аудиофайлы", "*.wav")])

   if not output_file:
      messagebox.showinfo('pz-mp3', 'Не указано имя сохраняемого файла')
      return
   try:
      cmd = ['ffmpeg', '-i', selected_file, '-ar', '8000', '-ac', '1', '-ab', '8k', '-c:a', 'libmp3lame', output_file]
      subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
      messagebox.showinfo('pz-mp3', 'Ухудшение завершено')
   except FileNotFoundError:
      messagebox.showerror('pz-mp3', 'Не найден ffmpeg')

window = ctk.CTk()
window.title("pz-mp3")
window.geometry("300x200")
window.resizable(False, False)
window.iconbitmap(default=sys.executable)

window.configure(fg_color="#141414")

label = ctk.CTkLabel(master=window, text="pz-mp3 - ухудшение качества звука", text_color="white", font=("Segoe UI", 16, "bold"))
label.place(relx=0.5, anchor="n")

file_button = ctk.CTkButton(master=window, text="обзор", font=("Segoe UI", 18, "bold"), command=file, fg_color="#f0793e", hover_color="#f05c3e", border_width=4, border_color="#ba471a", corner_radius=0, width=200, height=40)
file_button.pack(anchor="center", pady=60)

start_button = ctk.CTkButton(master=window, text="начать ухудшение", font=("Segoe UI", 18, "bold"), command=start, fg_color="#f0793e", hover_color="#f05c3e", border_width=4, border_color="#ba471a", corner_radius=0, width=200, height=40)
start_button.place(x=50, y=120)

window.mainloop()
