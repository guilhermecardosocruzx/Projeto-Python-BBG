import streamlit as st
from Materias import engenharia_eletrica

#definição de todos os inputs que vamos obter
aluno = []
ra = []
creditos = []
dia_livre = []
materias_cursadas = []
periodo = []

#listas de opções para os botões
periodo_all = ["manhã","tarde","noite","integral"]
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

######### AQUI É A LISTA ONDE SAIRÁ TODOS OS DADOS ATENÇÃO AQUI 
dados = [aluno, ra, creditos, materias_cursadas, dia_livre, periodo]


st.title("Planejador de Grade Universidade")

st.header("Selecione as matérias já cursadas:")

# Loop pelos semestres
for semestre, materias in engenharia_eletrica.items():
    with st.expander(f"Semestre {semestre}"):
        for materia in materias:
            if st.checkbox(materia.nome, key=f"{semestre}-{materia.nome}"):
                materias_cursadas.append(materia.nome)
#informações do aluno
st.header("Digite seus dados")
aluno = st.text_input("Nome do aluno:")
ra = st.number_input("RA do aluno:")  

#parametros do aluno
st.header("Quantos créditos deseja em sua grade?")
creditos = st.slider("Créditos desejados:", min_value=0, max_value=40, value=20)

#parametros do aluno
st.header("Preferências de Horário")
dia_livre = st.multiselect("Em quais dias você prefere não ter aula? (opcional)", dias_semana)
periodo = st.selectbox("Em qual período você estuda?",periodo_all)

#botão de confirmação, só aceita se obteve respostas em aluno, ra e periodo
if st.button("Enviar"):
    if aluno and ra and periodo:
        st.success("informações enviadas")	
    else:
        st.error("Nenhuma matéria selecionada.")
        st.warning("preencha os campos aluno, ra, periodo e créditos")

