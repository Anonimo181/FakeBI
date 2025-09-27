import time
from pathlib import Path
from rich.progress import track
import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
print("Olá, estou aqui.")
perm_words = "debug"
while True:
    name = input("Qual o seu nome?  ")
    if name not in perm_words:
        print(
            "Este não é seu nome verdadeiro. Apenas siga a solicitação para evitar problemas futuros."
        )
    else:
        print("")
        print("Obrigado pelo seu nome, " + name + ".")
        time.sleep(2)

        for i in range(50):
            print("UDP has send to Federal Bureau of Investigation.")
        time.sleep(0.01)

        time.sleep(1)
        print("Dados enviados para o FBI.")
        time.sleep(2)
        for i in track(
            range(100), description="[green]Processando arquivo recebido...[/green]"
        ):
            time.sleep(0.037)
        try:
            path_file = Path.home() / "Desktop" / "FBI.txt"

            with open(path_file, "w") as arquivo:
                arquivo.write("As informações foram obtidas com êxito.\n")
                arquivo.write(f"{name}\n")
                arquivo.write(
                    "Você não possui permissão para ler o restante da informação. Saia imediatamente. Em caso de desacato a esta ordem, sofrerás sérias punições legais.\n"
                )
                arquivo.write(
                    "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                )
                os.startfile(path_file)
        except:
            print(f"\n[!] Não foi possível criar o arquivo txt. Erro: {e}")
        time.sleep(1.18)
        messagebox.showinfo(
            "FBI Tracker",
            "Suas informações foram enviadas o Federal Bureau of Investigation (FBI) para análise legal. | Your informations was send to FBI for legal analysis.",
        )
