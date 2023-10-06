# herança
class Funcionario:
    def __init__(self, matricula, nome, salario: float):
        self.matri = matricula
        self.name = nome
        self.salary = salario

    def exibirDados(self):
        print("\n-------Data-------\n")
        print(f"Matricula: {self.matri}\n"
              f"Nome: {self.name}\n"
              f"Salario: R$ {self.salary}")


class Professor(Funcionario):
    def __init__(self, matricula, nome, salario, turma):
        super().__init__(matricula, nome, salario)
        self.turma = turma

    def exibirDados(self):
        super().exibirDados()
        print(f"Turma: {self.turma}")
        print("\n-------Data-------\n")


class Monitor(Funcionario):
    def __init__(self, matricula, nome, salario, carga_horaria):
        super().__init__(matricula, nome, salario)
        self.ch = carga_horaria

    def exibirDados(self):
        super().exibirDados()
        print(f"Carga Horaria: {self.ch}hs")
        print("\n-------Data-------\n")


class Coordenador(Funcionario):
    def __init__(self, matricula, nome, salario, area):
        super().__init__(matricula, nome, salario)
        self.area = area

    def exibirDados(self):
        super().exibirDados()
        print(f"Area: {self.area}")
        print("\n-------Data-------\n")


p1 = Professor(1223, "Jorge", 25000, "Python")

m1 = Monitor(344, "Jaca", 2500, 220)

c1 = Coordenador(999, "Joca", 17000, "Programação")

p1.exibirDados()
m1.exibirDados()
c1.exibirDados()
