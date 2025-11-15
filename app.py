import customtkinter 
import customtkinter as ctk 

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green")
app = ctk.CTk()

app.title("RecordaDose")
app.geometry("400x600")

def button_event():
    print("button pressed")

# ----- Funções dos Botoes -------  
def adicionarRemedio():
    print("Botão 'Adicionar um Remédio' pressionado")
    window_adicionar = ctk.CTkToplevel(app)
    window_adicionar.title("Adicionando um novo remédio")
    window_adicionar.geometry("350x350")
    window_adicionar.grab_set()


def verRemedio():
    print("Botão 'Ver Remédio' pressionado ")

def ExcluirRemedio():
    print("Botão 'excluir remedio' pressionado")
# ------------------ Fontes ------------------

fontePrincipal = ("Inter", 24, "bold")
fonteBotoes = ("Inter", 16)
fonteCampos = ("Inter", 14)

#--------------- Widgets dentro da nova janela ----- 

#------- Lista de Hora e Minuto ---------- 

listaHoras = [f"{h:02d}" for h in range(24)] 
listaMinutos = [f"{m:02d}" for m in range(60)]



def salvarRemedio(janela_para_fechar, entryNome, entryDosagem, comboboxHora, comboboxMinuto ):
    nome = entryNome.get()
    dosagem = entryDosagem.get()

    hora = comboboxHora.get()
    minuto = comboboxMinuto.get()

    horarioCompleto = f"{hora}:{minuto}"

    print("--- Novo Remédio Salvo! --- ")
    print(f"Nome: {nome}")
    print(f"Dosagem: {dosagem}")
    print(f"Horário: {horarioCompleto}")

    janela_para_fechar.destroy()






#Linha inicial do programa 


label_texto= ctk.CTkLabel(app, text="Seja bem vindo ao RecordaDose!", font=fontePrincipal)
label_texto.pack(pady=50)

botaoAdicionar = ctk.CTkButton(
    app, 
    text ="Adicionar um remédio",
    font=fonteBotoes,
    width=250, 
    height=40

)
botaoAdicionar.pack(pady=10)

botaoVer = ctk.CTkButton(
    app,
    text="Ver Remédios", 
    font=fonteBotoes,
    width=250,
    height=40,
)
botaoVer.pack(pady=10)


botaoExcluir = ctk.CTkButton(
    app,
    text="Excluir um remédio", 
    font=fonteBotoes,
    width=250,
    height=40 
)
botaoExcluir.pack(pady=10)










app.mainloop() #linha final do programa







