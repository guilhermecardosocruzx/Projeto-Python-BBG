class Materia:
    def __init__(self, creditos, dias, horarios, nome):  # Adicionado self como primeiro parâmetro
        self.nome = nome
        self.creditos = creditos
        self.dias = dias
        self.horarios = horarios
    
    def __str__(self):
        return f"{self.nome} | Créditos: {self.creditos} | Horários: {', '.join(self.horarios)} | Dias: {', '.join(self.dias)}"

# Matérias pré-criadas (note que a ordem dos parâmetros agora segue a do __init__)
CALCULO = Materia(
    creditos=6,
    dias=["Segunda", "Quarta"],
    horarios=["08:00-10:00", "14:00-16:00"],
    nome="Cálculo I"
)

ALGEBRA = Materia(
    creditos=4,
    dias=["Terça", "Quinta"],
    horarios=["10:00-12:00"],
    nome="Álgebra Linear"
)

Lista_materias = [CALCULO, ALGEBRA]