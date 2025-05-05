import pandas
class Materia:
    def __init__(self, creditos, dias, horarios, nome, precedencia):  # Adicionado self como primeiro parâmetro
        self.nome = nome
        self.creditos = creditos
        self.dias = dias
        self.horarios = horarios
        self.precedencia = precedencia

    def __str__(self):
        return f"{self.nome} | Créditos: {self.creditos} | Horários: {', '.join(self.horarios)} | Dias: {', '.join(self.dias)}"

# Matérias pré-criadas (note que a ordem dos parâmetros agora segue a do __init__)
CALCULOI = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00","19:00-21:00"],
    nome="Cálculo I",
    precedencia="nenhuma"
)

ALGEBRA = Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Álgebra Linear",
    precedencia="Geometria Analítica"
)
CALCULOII = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Cálculo II",
    precedencia="Cálculo I"
)
CALCULOIII = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Cálculo III",
    precedencia="Cálculo II"
)

FISICAI = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Física I",
    precedencia="nenhuma"
)

FISICAII = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Física II",
    precedencia="Física I"
)

FISICAIII = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Física III",
    precedencia="Física II"
)

GEOMETRIA = Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Geometria Analítica",
    precedencia="nenhuma"
)

CIRCUITOS = Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Circuitos Elétricos I",
    precedencia="nenhuma"
)

INTRODUCAO = Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Introdução à Engenharia",
    precedencia="nenhuma"
)

PROGRAMACAO = Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Programação",
    precedencia="nenhuma"
)

ELETRONICA = Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Eletrônica Básica",
    precedencia="nenhuma"
)

QUIMICA = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Química Geral",
    precedencia="nenhuma"
)

EXPRESSAO = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Expressão Gráfica",
    precedencia="nenhuma"
)

METODOLOGIA = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Metodologia científica",
    precedencia="nenhuma"
)

EQUACOES = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Equações Diferencias",
    precedencia="Cálculo III"
)

SINAIS_E_SISTEMAS = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Sinais e Sistemas",
    precedencia="Equações Diferenciais"
)

INSTRUMENTACAO = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Instrumentação",
    precedencia="Nenhuma"
)

ELETROMAGNETISMO = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Eletromagnetismo",
    precedencia="Física III"
)

ELETRONICA_ANALOGICA = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Eletrônica Analógica",
    precedencia="Circuitos Elétricos I"
)


ELETRONICA_DIGITAL = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Eletromagnetismo",
    precedencia="Eletrônica Analógica"
)

CIRCUITOSII= Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Circuitos Elétricos II",
    precedencia="Circuitos Elétricos I"
)


CONTROLE_LINEAR= Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Controle Linear",
    precedencia="Circuitos Elétricos II"
)

MICROCRONTROLADORES= Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Microcontroladores",
    precedencia="Controle Linear"
)

MAQUINAS_ELETRICASI= Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Máquinas Elétricas I",
    precedencia="Eletrônica Básica"
)

MAQUINAS_ELETRICASII= Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Máquinas Elétricas II",
    precedencia="Máquinas Elétricas I"
)

INSTALACOES= Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Instalações Elétricas",
    precedencia="Circuitos Elétricos I"
)

PROBABILIDADE = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Probabilidade e Estatística",
    precedencia="Cálculo I"
)

FENOMENOS_DE_TRANSPORTE = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Fenômenos de Transporte",
    precedencia="Física II"
)
COMUNICACOES_ANALOGICAS = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Comunicações Analógicas",
    precedencia="Eletrônica Analógica"
)

PROCESSAMENTO_SINAIS = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Processamento de sinais",
    precedencia="Sinais e Sistemas"
)

AUTOMACAO_INDUSTRIAL = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Automação Industrial",
    precedencia="Eletrônica Digital"
)

GESTAO_PROJETOS = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Gestão de Projetos",
    precedencia="nenhuma"
)

CONVERSAO_ENERGIA = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Conversão de Energia",
    precedencia="Eletromagnetismo"
)

SISTEMAS_POTENCIAS = Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Sistemas de potência",
    precedencia="Sinais e Sistemas"
)

ETICA_LEGISLACAO= Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Ética e Legislação",
    precedencia="nenhuma"
)

SISTEMAS_DE_CONTROLE= Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Sistemas de controle",
    precedencia="Controle Linear"
)

ELETRONICA_POTENCIA= Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Eletrônica de Potência",
    precedencia="Eletrônica analógica"
)

TCCI= Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Trabalho de Conclusão de Curso I",
    precedencia="nenhuma"
)

ENERGIA= Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Energia e Meio Ambiente",
    precedencia="nenhuma"
)

PROJETO= Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Projeto de Engenharia Elétrica I",
    precedencia="nenhuma"
)

PROJETOII = Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Projeto de Engenharia Elétrica II",
    precedencia="Projeto de Engenharia Elétrica I"
)

OPTATIVAI = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Optativa I",
    precedencia="nenhuma"
)

OPTATIVAII = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Optativa II",
    precedencia="nenhuma"
)

OPTATIVAIII = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Optativa III",
    precedencia="nenhuma"
)

ESTAGIO = Materia(
    creditos=2,
    dias=["Segunda"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Estágio Supervisionado",
    precedencia="nenhuma"
)

EMPREENDEDORISMO= Materia(
    creditos=2,
    dias=["Terça"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Empreendedorismo",
    precedencia="nenhuma"
)

TCCII = Materia(
    creditos=2,
    dias=["Quarta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Trabalho de Conclusão de Curso II",
    precedencia="Trabalho de Conclusão de Curso I"
)

DESENHO_TECNICO = Materia(
    creditos=2,
    dias=["Quinta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Desenho Técnico",
    precedencia="nenhuma"
)

OPTATIVAIV = Materia(
    creditos=2,
    dias=["Sexta"],
    horarios=["08:00-10:00", "14:00-16:00", "19:00-21:00"],
    nome="Optativa IV",
    precedencia="nenhuma"
)


# Dicionário contentendo todos os as materias (objects) do curso engenharia eletrica
# Indice do dict corresponde ao périodo do curso, nesse caso semestre. 
engenharia_eletrica = {
    1: [CALCULOI, FISICAI, GEOMETRIA, INTRODUCAO, PROGRAMACAO],
    2: [CALCULOII, FISICAII, ALGEBRA, QUIMICA, EXPRESSAO],
    3: [CALCULOIII, FISICAIII, CIRCUITOS, ELETRONICA, METODOLOGIA],
    4: [EQUACOES, SINAIS_E_SISTEMAS, INSTRUMENTACAO, ELETROMAGNETISMO, PROBABILIDADE],
    5: [ELETRONICA_ANALOGICA, ELETRONICA_DIGITAL, CIRCUITOSII, CONTROLE_LINEAR],
    6: [MICROCRONTROLADORES, MAQUINAS_ELETRICASI, INSTALACOES, FENOMENOS_DE_TRANSPORTE],
    7: [COMUNICACOES_ANALOGICAS, PROCESSAMENTO_SINAIS, AUTOMACAO_INDUSTRIAL, GESTAO_PROJETOS],
    8: [CONVERSAO_ENERGIA, SISTEMAS_POTENCIAS, ETICA_LEGISLACAO, SISTEMAS_DE_CONTROLE],
    9: [ELETRONICA_POTENCIA, TCCI, ENERGIA, PROJETO],
    10: [PROJETOII, OPTATIVAI, OPTATIVAII, OPTATIVAIII, ESTAGIO, TCCII, EMPREENDEDORISMO, DESENHO_TECNICO, OPTATIVAIV],
}

#criando um df
dados = []

for semestre, materias in engenharia_eletrica.items():
    for materia in materias:
        dados.append({
            "Semestre": semestre,
            "Nome": materia.nome,
            "Créditos": materia.creditos,
            "Dias": ", ".join(materia.dias),
            "Horários": ", ".join(materia.horarios),
            "Precedência": materia.precedencia
        })

df = pandas.DataFrame(dados)