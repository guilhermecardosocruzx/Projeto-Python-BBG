def monta_grade(dados_aluno):
    from Materias import df

    # Definição dos horários possíveis para cada período
    periodo_horarios = {
        "manhã": ["08:00-10:00"],
        "tarde": ["14:00-16:00"],
        "noite": ["19:00-21:00"],
        "integral": ["08:00-10:00", "14:00-16:00", "19:00-21:00"]
    }

    # Coleta os dados fornecidos pelo aluno
    materias_cursadas = dados_aluno["materias_cursadas"]
    dias_livres = dados_aluno["dia_livre"]
    creditos_desejados = dados_aluno["creditos"]
    periodo = dados_aluno["periodo"]

    # Filtra as matérias restantes que o aluno ainda não cursou
    materias_restantes = df[~df["Nome"].isin(materias_cursadas)]

    # Variáveis para armazenar as informações da grade
    grade_montada = []
    total_creditos = 0
    horarios_ocupados = set()

    # Iteração por semestre e pelas matérias dentro de cada semestre
    for semestre in sorted(materias_restantes["Semestre"].unique()):
        materias_semestre = materias_restantes[materias_restantes["Semestre"] == semestre]
        for _, materia in materias_semestre.iterrows():
            nome = materia["Nome"]
            creditos = materia["Créditos"]
            dias = materia["Dias"].split(", ")  # Dias da matéria
            todos_horarios = materia["Horários"].split(", ")  # Horários disponíveis para a matéria
            precedencia = materia["Precedência"]

            # Verifica se todos os dias da matéria estão livres
            if any(dia in dias_livres for dia in dias):
                continue


            # Verifica se a matéria tem precedência e se o aluno já cursou a matéria pré-requisito
            if precedencia != "nenhuma" and precedencia not in materias_cursadas:
                continue

            conflito = False
            horarios_disponiveis = []
            dia_horarios_usados = {}

            # Caso o aluno tenha escolhido o período integral
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

                dia_horarios_usados = {}
                for dia in dias:
                    horario_encontrado = None
                    for horario in horarios_disponiveis:
                        chave = f"{dia}|{horario}"
                        if chave not in horarios_ocupados:
                            dia_horarios_usados[dia] = horario
                            horario_encontrado = horario
                            break
                    if not horario_encontrado:
                        conflito = True
                        break

            # Se houver conflito ou se não houver horários disponíveis, ignora a matéria
            if conflito or not horarios_disponiveis:
                continue

            # Verifica se o total de créditos será excedido
            if total_creditos + creditos <= creditos_desejados:
                grade_montada.append({
                    "Nome": nome,
                    "Créditos": creditos,
                    "Dias": dias,
                    "Horários": [dia_horarios_usados[d] for d in dias]
                })
                total_creditos += creditos

                # Marca os horários como ocupados
                for dia in dias:
                    if periodo == "integral":
                        horario = dia_horarios_usados.get(dia)
                        if horario:
                            horarios_ocupados.add(f"{dia}|{horario}")
                    else:
                        for horario in horarios_disponiveis:
                            horarios_ocupados.add(f"{dia}|{horario}")

            # Se já atingiu os créditos desejados, sai do loop
            if total_creditos >= creditos_desejados:
                break  # Sai do loop interno se já atingir os créditos

        # Se já atingiu os créditos desejados, sai também do loop externo
        if total_creditos >= creditos_desejados:
            break

    # Exibe as matérias na grade montada
    print("Grade Montada: \n")
    for materia in grade_montada:
        nome = materia["Nome"]
        dias = materia["Dias"]
        horarios = materia["Horários"]
        print(f"✅ Matéria: {nome}")
        for dia, horario in zip(dias, horarios):
            print(f"Dia: {dia}")
            print(f"Horário: {horario}")
        print(f"Créditos: {materia['Créditos']}")
        print("-" * 40)

    return grade_montada