import tkinter as tk
from ollama_manager import install_or_repair_ollama, move_to_external_drive, ensure_models

def run_all():
    install_or_repair_ollama()
    move_to_external_drive()
    ensure_models()

root = tk.Tk()
root.title("Ollama All-in-One")

btn = tk.Button(root, text="Rulează Configurare Completă", command=run_all, height=3, width=30)
btn.pack(pady=20)

root.mainloop()
