import pandas
from Inputs import inputs, output
import streamlit as st
import grid
import json

if __name__ == "__main__":

    inputs()
    #Primeiro é feito um try para saber se dentro da pasta existe o arquivo dados.json criado pelos inputs
    try:
        with open("dados.json", "r", encoding="utf-8") as f:
            dados_aluno = json.load(f)

        print("✅ Dados recebidos do aluno:")
        for chave, valor in dados_aluno.items():
            print(f"{chave}: {valor}")

        grade = grid.monta_grade(dados_aluno)
        

    except FileNotFoundError:
        #Se nenhum arquivo for encontrado a mensagem abaixo é lançada
        print("❌ Arquivo 'dados.json' não encontrado. Execute primeiro o Inputs.py via Streamlit.")

