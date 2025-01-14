# Superclasse
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        return "Som genérico de animal"

# Subclasse
class Cachorro(Animal):
    def som(self):  # Sobrescrevendo o método 'som'
        return "Au au"

# Outra Subclasse
class Gato(Animal):
    def som(self):  # Sobrescrevendo o método 'som'
        return "Miau"

# Usando as classes
animal = Animal("Genérico")
print(f"{animal.nome} faz: {animal.som()}")  # Som genérico de animal

cachorro = Cachorro("Rex")
print(f"{cachorro.nome} faz: {cachorro.som()}")  # Au au

gato = Gato("Mimi")
print(f"{gato.nome} faz: {gato.som()}")  # Miau
