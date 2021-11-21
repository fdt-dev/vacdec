#!/usr/bin/env python3
# -*- coding: cp1252 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.scrolledtext as st
from vacdec import *

top = tk.Tk()
result = st.ScrolledText(top, wrap = tk.WORD, width = 80, height = 20)

def vacdec_gui():
    # open button
    open_button = ttk.Button(
        top,
        text='Datei öffnen ...',
        command=select_file
    )

    open_button.grid(row=0, column=0)

    top.title("Digitales CoViD-Zertifikat - Decoder")

    result.grid(row=2, column=0, columnspan=6)

    open_button.focus()

    top.mainloop()


def select_file():
    filetypes = (
        ('Portable Network Graphics (PNG)', '*.png'),
        ('Joint Photographic Experts Group (JPG)', '*.jpg'),
        ('Alle Dateien', '*.*')
    )

    filename = fd.askopenfilename(
        title='Datei öffnen ...',
        initialdir='.',
        filetypes=filetypes)

    call_vacdec(filename)


def call_vacdec(filename):
    data = decode_image(filename)
    json_result = ppformat_vacdec(vacdecode(data))
    result.delete(1.0, tk.END)
    result.insert('insert', json_result)
    

if __name__ == "__main__":
    vacdec_gui()
