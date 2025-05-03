import streamlit as st
from Materias import engenharia_eletrica
import pandas 
import json

def inputs():
    # Inicializa o estado da "página"
    if "pagina" not in st.session_state:
        st.session_state.pagina = "formulario"

    # ===================== PÁGINA 1 ============================
    if st.session_state.pagina == "formulario":
        
        # listas de opções para os botões
        aluno = []
        ra = []
        creditos = []
        dia_livre = []
        materias_cursadas = []
        periodo = []
        materias_cursadas = []
        periodo_all = ["manhã", "tarde", "noite", "integral"]
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

        st.title("Planejador de Grade Universidade")

        # informações do aluno
        st.header("Digite seus dados")
        aluno = st.text_input("Nome do aluno:").upper()
        ra = st.number_input("RA do aluno:", step=1)

        # parâmetros do aluno
        st.header("Quantos créditos deseja em sua grade?")
        creditos = st.slider("Créditos desejados:", min_value=0, max_value=40, value=20)

        st.header("Preferências de Horário")
        dia_livre = st.multiselect("Em quais dias você prefere não ter aula? (opcional)", dias_semana)
        periodo = st.selectbox("Em qual período você estuda?", periodo_all)

        st.header("Selecione as matérias já cursadas:")
        # Loop pelos semestres
        for semestre, materias in engenharia_eletrica.items():
            with st.expander(f"Semestre {semestre}"):
                for materia in materias:
                    if st.checkbox(materia.nome, key=f"{semestre}-{materia.nome}"):
                        materias_cursadas.append(materia.nome)

        # botão de confirmação
        if st.button("Enviar"):
            if aluno and ra and periodo:
                dados_dict = {
                    "aluno": aluno,
                    "ra": ra,
                    "creditos": creditos,
                    "materias_cursadas": materias_cursadas,
                    "dia_livre": dia_livre,
                    "periodo": periodo
                }  
                #envia informações via json
                with open("dados.json", "w", encoding="utf-8") as f:
                    json.dump(dados_dict, f, ensure_ascii=False, indent=4)
                    
                st.success("Informações enviadas e salvas com sucesso!")
                st.session_state.pagina = "resultado" # Muda para a "página" de resultado
                st.rerun()
            else:
                st.error("Confira os campos aluno, ra e periodo")

    elif st.session_state.pagina == "resultado":

        st.title("Informações salvas com sucesso!")

        if st.button("Ver dados salvos"):
            output()

        if st.button("Voltar"):
            st.session_state.pagina = "formulario"
            st.rerun()    
def output():
    # Abrir e carregar o JSON salvo
    with open("dados.json", "r", encoding="utf-8") as leitura:
        dados = json.load(leitura)

    # Transformar em DataFrame (usando .items() se for um dicionário simples)
    df = pandas.DataFrame([dados])  # [] garante que cada entrada seja uma linha

    # Exibir no Streamlit
    st.header("Dados do Aluno")
    st.dataframe(df, hide_index=1)
