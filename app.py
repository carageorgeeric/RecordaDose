import customtkinter 
import customtkinter as ctk 

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green")
app = ctk.CTk()

app.title("RecordaDose")
app.geometry("400x600")

def button_event():
    print("button pressed")


#Linha inicial do programa 


label_texto= ctk.CTkLabel(app, text="Seja bem vindo ao RecordaDose!", font=("Arial", 20,))
label_texto.pack(pady=50)












app.mainloop() #linha final do programa







