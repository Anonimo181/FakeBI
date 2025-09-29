import time
from pathlib import Path
from rich.progress import track
import os
import tkinter as tk
from tkinter import (
    messagebox,
    simpledialog,
    Toplevel,
    Listbox,
    Entry,
    Button,
    Checkbutton,
    Frame,
    Label,
    END,
    ANCHOR,
    BooleanVar,
)

# Variável global para nomes permitidos
allow_names = {"debug"}


def main_logic():
    """
    Contém a lógica principal do programa.
    Toda a interação aqui deve ser APENAS via terminal.
    """
    print("Olá, estou aqui.")
    while True:
        # CORREÇÃO: Usar input() para interação via terminal.
        # O .strip() remove espaços em branco extras.
        name = input("Qual o seu seu nome? ").strip()

        if not name:
            # Lida com o caso de entrada vazia
            print("Nome não pode ser vazio. Tente novamente.")
            continue

        if name not in allow_names:
            print("Este nome não consta na identidade registrada. Tente novamente.")
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
            # O 'track' da biblioteca rich é uma barra de progresso de terminal, o que é permitido.
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
            except Exception as e:
                print(f"\n[!] Não foi possível criar o arquivo txt. Erro: {e}")

            time.sleep(1.18)
            # CORREÇÃO: Substituído messagebox.showinfo (GUI) por print (Terminal)
            print(
                "Suas informações foram enviadas o Federal Bureau of Investigation (FBI) para análise legal. | Your informations was send to FBI for legal analysis."
            )
            break


def start_program(root):
    """Destrói a GUI do menu e inicia a lógica principal no terminal."""
    root.destroy()
    main_logic()


def open_config_window(root):
    """Função para abrir a janela de configuração (GUI permitida para o menu)."""
    root.withdraw()
    config_window = Toplevel(root)
    config_window.title("Configuração de Nomes")
    config_window.geometry("350x400")
    config_window.resizable(False, False)

    list_frame = Frame(config_window)
    list_frame.pack(pady=10, padx=10, fill="both", expand=True)

    listbox_label = Label(list_frame, text="Nomes Permitidos:")
    listbox_label.pack(anchor="w")

    names_listbox = Listbox(list_frame)
    names_listbox.pack(fill="both", expand=True)

    def update_listbox():
        names_listbox.delete(0, END)
        for name in sorted(list(allow_names)):
            names_listbox.insert(END, name)

    update_listbox()

    entry_frame = Frame(config_window)
    entry_frame.pack(pady=5, padx=10, fill="x")

    name_entry = Entry(entry_frame)
    name_entry.pack(side="left", fill="x", expand=True)

    def add_name_action():
        new_name = name_entry.get().strip()
        if new_name and new_name not in allow_names:
            allow_names.add(new_name)
            update_listbox()
            name_entry.delete(0, END)

    add_button = Button(entry_frame, text="Adicionar", command=add_name_action)
    add_button.pack(side="right", padx=(5, 0))

    def remove_name_action():
        selected_indices = names_listbox.curselection()
        if not selected_indices:
            return

        selected_name = names_listbox.get(selected_indices[0])

        if selected_name == "debug" and not allow_debug_removal.get():
            messagebox.showerror(
                "Protegido",
                "O nome 'debug' não pode ser removido a menos que a opção seja marcada.",
            )
            return

        allow_names.remove(selected_name)
        update_listbox()

    remove_button = Button(
        config_window, text="Remover Selecionado", command=remove_name_action
    )
    remove_button.pack(pady=5, padx=10, fill="x")

    allow_debug_removal = BooleanVar(value=False)
    debug_check = Checkbutton(
        config_window,
        text="Permitir alteração do nome 'debug'",
        variable=allow_debug_removal,
    )
    debug_check.pack(pady=5, padx=10, anchor="w")

    def close_config():
        config_window.destroy()
        root.deiconify()

    back_button = Button(config_window, text="Voltar", command=close_config)
    back_button.pack(pady=10, padx=10, fill="x")

    config_window.protocol("WM_DELETE_WINDOW", close_config)


def main():
    """Cria e exibe a GUI do menu inicial (única GUI permitida)."""
    root = tk.Tk()
    root.title("Tela Inicial")
    root.geometry("300x150")
    root.resizable(False, False)

    main_frame = Frame(root, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)

    start_button = Button(main_frame, text="Start", command=lambda: start_program(root))
    start_button.pack(fill="x", pady=5)

    config_button = Button(
        main_frame, text="Config", command=lambda: open_config_window(root)
    )
    config_button.pack(fill="x", pady=5)

    exit_button = Button(main_frame, text="Exit", command=root.destroy)
    exit_button.pack(fill="x", pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
