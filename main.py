class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.nome, " esta emitindo o som: ", self.som)

    def mudar_cor(self, nova_cor):
        nova_cor = input("Digite a nova cor: ")

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        self.tamanho = tamanho
        super().__init__(nome, idade, especie, cor, som)

    def trombar(self):
        print("O elefante faz o som: ", self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

aux_nome = input("Entre com o nome do elefante: ")
aux_idade = input("Entre com a idade do elefante: ")
aux_especie = input("Entre com a especie do elefante: ")
aux_cor = input("Entre com a cor do elefante: ")
aux_som = input("Entre com o som do elefante: ")
aux_tamanho = input("Entre com o tamanho do elefante: ")

elefante1 = Elefante(aux_nome, aux_idade, aux_especie, aux_cor, aux_som, aux_tamanho)

if elefante1.especie == "Africano":
    if elefante1.idade < '10':
        elefante1.mudar_tamanho("pequeno")
        elefante1.som = "Paaah"

    elif elefante1.idade > '10':
        elefante1.mudar_tamanho("grande")
        elefante1.som = "PAHHHHHH"

print("O som do elefante: ", elefante1.som, " e o tamanho são: ", elefante1.tamanho)

