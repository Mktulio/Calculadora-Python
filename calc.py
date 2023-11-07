# Inicio

import tkinter as tk
import math
from tkinter import Entry, INSERT

# Função para avaliar expressões matemáticas

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, "end")
        entry.insert(INSERT, str(result))
        history.insert("end", f"{expression} = {result}\n")
    except Exception as e:
        entry.delete(0, "end")
        entry.insert(INSERT, "Erro")
        history.insert("end", f"Erro: {str(e)}\n")

# Função para adicionar caracteres à entrada

def append_to_input(char):
    current_text = entry.get()
    entry.delete(0, "end")
    entry.insert(INSERT, current_text + char)

# Função para limpar a entrada

def clear_input():
    entry.delete(0, "end")

# Configuração da janela

root = tk.Tk()
root.title("Calculadora")

# Criação da entrada de texto

entry = Entry(root, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)
entry.bind("<Return>", lambda event: evaluate_expression())

# Criação dos botões
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row, col = 1, 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, command=evaluate_expression, height=2, width=6).grid(row=row, column=col)
    elif button == "C":
        tk.Button(root, text=button, command=clear_input, height=2, width=6).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda b=button: append_to_input(b), height=2, width=6).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Criação da área de histórico
history = tk.Text(root, height=10, width=30)
history.grid(row=5, column=0, columnspan=4)

root.mainloop()
