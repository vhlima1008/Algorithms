class Dojo:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor:
            self._nome = valor
        else:
            raise ValueError('Nome deve ser uma string não vazia.')

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor
        else: 
            raise ValueError('Idade deve ser um numero positivo.')
        
pesso = Dojo('', 2000)
print(pesso.nome, pesso.idade)