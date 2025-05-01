import pandas as pd
from Materias import df
import json

def engenharia_eletrica(dados_aluno):
    """
    Gera uma grade com o maior número possível de matérias dentro do limite de créditos,
    respeitando:
    - Dias livres
    - Precedências
    - Conflitos de horário
    - Compatibilidade com o período (manhã, tarde, noite, integral)
    Nesta Ordem, eu percebi que existem certos problemas 
    """

    from Materias import df

    periodo_horarios = {
        "manhã": ["08:00-10:00"],
        "tarde": ["14:00-16:00"],
        "noite": ["19:00-21:00"],
        "integral": ["08:00-10:00", "14:00-16:00", "19:00-21:00"]
    }

    materias_cursadas = dados_aluno["materias_cursadas"]
    dias_livres = dados_aluno["dia_livre"]
    creditos_desejados = dados_aluno["creditos"]
    periodo = dados_aluno["periodo"]

    materias_restantes = df[~df["Nome"].isin(materias_cursadas)]

    grade_montada = []
    total_creditos = 0
    horarios_ocupados = set()

    for _, materia in materias_restantes.iterrows():
        nome = materia["Nome"]
        creditos = materia["Créditos"]
        dias = materia["Dias"].split(", ")
        todos_horarios = materia["Horários"].split(", ")
        precedencia = materia["Precedência"]

        # Ignorar se a matéria só ocorre em dias livres
        if set(dias).issubset(set(dias_livres)):
            continue

        # Ignorar se precedência não foi cumprida
        if precedencia.lower() != "nenhuma" and precedencia not in materias_cursadas:
            continue

        conflito = False
        horarios_disponiveis = []
        dia_horarios_usados = {}

     #Separei a parte do período integral das outras no algoritmo
        if periodo == "integral":
            horarios_validos = periodo_horarios["integral"]
            for dia in dias:
                horario_encontrado = None
                for horario in horarios_validos:
                    chave = f"{dia}|{horario}"
                    if chave not in horarios_ocupados and horario in todos_horarios:
                        horario_encontrado = horario
                        break
                if horario_encontrado:
                    horarios_disponiveis.append(horario_encontrado)
                    dia_horarios_usados[dia] = horario_encontrado
                else:
                    conflito = True
                    break
        else:
            horarios_validos = periodo_horarios.get(periodo, [])
            horarios_disponiveis = [h for h in todos_horarios if h in horarios_validos]
            for dia in dias:
                for horario in horarios_disponiveis:
                    if f"{dia}|{horario}" in horarios_ocupados:
                        conflito = True

        if conflito or not horarios_disponiveis:
            continue

        if total_creditos + creditos <= creditos_desejados:
            grade_montada.append({
                "Nome": nome,
                "Créditos": creditos,
                "Dias": dias,
                "Horários": horarios_disponiveis if periodo != "integral" else [dia_horarios_usados[d] for d in dias]
            })
            total_creditos += creditos

            # Marcar horários ocupados
            for dia in dias:
                if periodo == "integral":
                    horario = dia_horarios_usados.get(dia)
                    if horario:
                        horarios_ocupados.add(f"{dia}|{horario}")
                else:
                    for horario in horarios_disponiveis:
                        horarios_ocupados.add(f"{dia}|{horario}")

    #Print da grade final
    print("\n📘 Grade sugerida:")
    for m in grade_montada:
        print(f"• {m['Nome']} ({m['Créditos']} créditos)")
        print(f"  Dias: {', '.join(m['Dias'])}")
        print(f"  Horários: {', '.join(m['Horários'])}")
        print("-" * 30)

    print(f"\nTotal de créditos: {total_creditos}")

    return grade_montada





if __name__ == "__main__":
    #Primeiro é feito um try para saber se dentro da pasta existe o arquivo dados.json criado pelos inputs
    try:
        with open("dados.json", "r", encoding="utf-8") as f:
            dados_aluno = json.load(f)

        print("✅ Dados recebidos do aluno:")
        for chave, valor in dados_aluno.items():
            print(f"{chave}: {valor}")
        engenharia_eletrica(dados_aluno)


    except FileNotFoundError:
        #Se nenhum arquivo for encontrado a mensagem abaixo é lançada
        print("❌ Arquivo 'dados.json' não encontrado. Execute primeiro o Inputs.py via Streamlit.")

