import customtkinter as ctk
import threading
import time
import datetime
import platform
import winsound  

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("RecordaDose")
app.geometry("400x600")


listaRemedios = []   


def iniciar_notificacoes():
    def verificar_notificacoes():
        while True:
            agora = datetime.datetime.now().strftime("%H:%M")
            for remedio in listaRemedios:
                if remedio["horario"] == agora:
                    mostrar_notificacao(remedio)
            time.sleep(30)

    thread = threading.Thread(target=verificar_notificacoes, daemon=True)
    thread.start()


def mostrar_notificacao(remedio):
    notif = ctk.CTkToplevel()
    notif.title("RecordaDose - Hora do Remédio")
    notif.geometry("300x150")

    texto = f"Está na hora de tomar:\n\n{remedio['nome']}\n{remedio['dosagem']}"
    label = ctk.CTkLabel(notif, text=texto, font=("Inter", 16))
    label.pack(pady=20)

    botao = ctk.CTkButton(notif, text="OK", command=notif.destroy)
    botao.pack(pady=10)

   
    if platform.system() == "Windows":
        winsound.Beep(1000, 600)




def adicionarRemedio():

    window = ctk.CTkToplevel(app)
    window.title("Adicionar Remédio")
    window.geometry("350x400")
    window.grab_set()


    ctk.CTkLabel(window, text="Nome do remédio:", font=("Inter", 14)).pack(pady=5)
    entryNome = ctk.CTkEntry(window, width=250)
    entryNome.pack()

    ctk.CTkLabel(window, text="Dosagem (ex: 500mg):", font=("Inter", 14)).pack(pady=5)
    entryDosagem = ctk.CTkEntry(window, width=250)
    entryDosagem.pack()


    listaHoras = [f"{h:02d}" for h in range(24)]
    listaMinutos = [f"{m:02d}" for m in range(60)]

    frameHorario = ctk.CTkFrame(window)
    frameHorario.pack(pady=20)

    comboboxHora = ctk.CTkComboBox(frameHorario, values=listaHoras, width=80)
    comboboxHora.grid(row=0, column=0, padx=5)
    comboboxMinuto = ctk.CTkComboBox(frameHorario, values=listaMinutos, width=80)
    comboboxMinuto.grid(row=0, column=1, padx=5)


    botaoSalvar = ctk.CTkButton(
        window,
        text="Salvar Remédio",
        command=lambda: salvarRemedio(window, entryNome, entryDosagem,
                                      comboboxHora, comboboxMinuto)
    )
    botaoSalvar.pack(pady=20)



def salvarRemedio(janela, entryNome, entryDosagem, comboboxHora, comboboxMinuto):
    nome = entryNome.get()
    dosagem = entryDosagem.get()
    horario = f"{comboboxHora.get()}:{comboboxMinuto.get()}"

    if nome.strip() == "":
        return

    novo = {
        "nome": nome,
        "dosagem": dosagem,
        "horario": horario
    }

    listaRemedios.append(novo)
    print("Remédio salvo!", novo)

    janela.destroy()



def verRemedio():

    window = ctk.CTkToplevel(app)
    window.title("Lista de Remédios")
    window.geometry("350x400")
    window.grab_set()

    for remedio in listaRemedios:
        texto = f"{remedio['nome']} - {remedio['dosagem']} - {remedio['horario']}"
        label = ctk.CTkLabel(window, text=texto, font=("Inter", 14))
        label.pack(pady=5)


def excluirRemedio():

    window = ctk.CTkToplevel(app)
    window.title("Excluir Remédio")
    window.geometry("350x400")
    window.grab_set()

    ctk.CTkLabel(window, text="Selecione um remédio para excluir:", font=("Inter", 14)).pack(pady=10)

    listaNomes = [rem["nome"] for rem in listaRemedios]

    if not listaNomes:
        ctk.CTkLabel(window, text="Nenhum remédio cadastrado.", font=("Inter", 14)).pack()
        return

    combo = ctk.CTkComboBox(window, values=listaNomes)
    combo.pack(pady=10)

    botao = ctk.CTkButton(
        window,
        text="Excluir",
        command=lambda: remover(window, combo.get())
    )
    botao.pack(pady=20)


def remover(janela, nome):
    global listaRemedios
    listaRemedios = [r for r in listaRemedios if r["nome"] != nome]
    janela.destroy()




label_texto = ctk.CTkLabel(app, text="RecordaDose", font=("Inter", 28, "bold"))
label_texto.pack(pady=50)

botaoAdicionar = ctk.CTkButton(app, text="Adicionar um Remédio", font=("Inter", 16),
                               width=250, height=40, command=adicionarRemedio)
botaoAdicionar.pack(pady=10)

botaoVer = ctk.CTkButton(app, text="Ver Remédios", font=("Inter", 16),
                         width=250, height=40, command=verRemedio)
botaoVer.pack(pady=10)

botaoExcluir = ctk.CTkButton(app, text="Excluir um Remédio", font=("Inter", 16),
                             width=250, height=40, command=excluirRemedio)
botaoExcluir.pack(pady=10)


iniciar_notificacoes()

app.mainloop()
