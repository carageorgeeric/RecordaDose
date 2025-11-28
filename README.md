# 💊 RecordaDose

> **Projeto de Extensão da Universidade Estácio de Sá** > **Disciplina:** Tópicos de Big Data em Python (2º Semestre)

## 📖 Sobre o Projeto

O **RecordaDose** é uma aplicação desktop desenvolvida em Python destinada a auxiliar utilizadores no controlo da medicação. O objetivo principal é fornecer uma interface simples e amigável para registar, visualizar e gerir horários de remédios, garantindo que o tratamento seja seguido corretamente.

Este projeto foca-se na utilização de bibliotecas modernas de interface gráfica e manipulação de tempo/threads para alertas sonoros.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica:** `customtkinter` (Design moderno e responsivo)
* **Manipulação de Tempo:** `datetime`, `time`
* **Concorrência:** `threading` (Para verificação de alarmes em segundo plano)
* **Sistema/Sons:** `platform`, `winsound` (Alerta sonoro em ambiente Windows)

## ✨ Funcionalidades

O sistema conta com um menu principal intuitivo com as seguintes opções:

* **➕ Adicionar Remédio:**
    * Campo para inserir o nome do medicamento.
    * Seletor de horário (Formato 24h).
    * Confirmação de registo.
* **📋 Ver Remédios:**
    * Listagem de todos os medicamentos cadastrados.
    * Visualização dos horários definidos.
    * Opção de **Edição** (alterar nome ou horário).
* **🗑️ Excluir Remédios:**
    * Listagem para seleção.
    * Botão para remover medicamentos da lista.


1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/RecordaDose.git](https://github.com/SEU-USUARIO/RecordaDose.git)
