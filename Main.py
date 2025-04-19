class Materia:
    def __init__(self, creditos, dias, horarios, nome, precedencia):  # Adicionado self como primeiro parâmetro
        self.nome = nome
        self.creditos = creditos
        self.dias = dias
        self.horarios = horarios
        self.precedencia = precedencia
    
    def __str__(self):
        return f"{self.nome} | Créditos: {self.creditos} | Dias: {', '.join(self.dias)} | Horários: {', '.join(self.horarios)} | Precedencia: {self.precedencia}"

# Matérias pré-criadas (note que a ordem dos parâmetros agora segue a do __init__)
CALCULO = Materia(
    creditos=6,
    dias=["Segunda", "Quarta"],
    horarios=["08:00-10:00", "14:00-16:00"],
    nome="Cálculo I",
    precedencia="nenhuma"
)

ALGEBRA = Materia(
    creditos=4,
    dias=["Terça", "Quinta"],
    horarios=["10:00-12:00"],
    nome="Álgebra Linear",
    precedencia="nenhuma"
)

Lista_materias = [CALCULO, ALGEBRA]

if __name__ == "__main__":
     print("Matérias disponíveis:")
     for i, materia in enumerate(Lista_materias, 1):
        print(f"\n{i}. {materia}")
'''
A gente pode agora criar os cursos com suas materias, ai a gente cria o dicionario, no qual a chave seja o nome
do curso, e seu conteudo uma lista com suas materias, como a Lista_materias que eu usei de exp
'''