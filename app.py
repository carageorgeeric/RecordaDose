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

def verRemedio():
    print("Botão 'Ver Remédio' pressionado ")

def ExcluirRemedio():
    print("Botão 'excluir remedio' pressionado")
# ------------------ Fontes ------------------

fontePrincipal = ("Inter", 24, "bold")
fonteBotoes = ("Inter", 16)

#--------------------------------------------

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







