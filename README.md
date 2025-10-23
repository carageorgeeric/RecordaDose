# RecordaDose
Projeto de Extensão da Universidade Estácio de Sá. Segundo Semestre da matéria Tópicos de Big Data em Python 



Tarefas a fazer 



24/10 - Criar primeira tela com butoes funcionais 
- texto "Seja bem vindo ao recorda dose" 
- Botoes: Adicionar Remedio, Ver Remedios, Excluir Remedios 

adicionar remedio -> campo para digitar o nome e selecionar horario e botao de confirmar (depois salva em uma matriz)
ver remedios -> mostrar os remedios adicionados, os horarios e permitir edicao de nome e horario 
excluir remedios -> mostrar todos os remedios, e dar a opção de excluir 

OBS -> Horarios com formato de 24 horas  



DICAS 
- ADICIONAR TEXTO: 
texto = ctk.CTkLabel(app, text="Olá, bem-vindo ao RecordaDose!")
texto.pack(pady=20)

- ADICIONAR BOTAO: 
botao = ctk.CTkButton(app, text="Clique aqui")
botao.pack(pady=10)

- MUDAR FONTES E TAMANHOS:
texto = ctk.CTkLabel(
    app,
    text="Olá, bem-vindo ao RecordaDose!",
    font=("Arial", 20,)  # ← (fonte, tamanho, estilo) (a fonte deve estar instalada no pc)
    text_color="#2ecc71" -> (Mudando a cor do texto)
)
texto.pack(pady=30)

- 