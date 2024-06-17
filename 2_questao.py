class AutomatoFinito:
    def __init__(self, transicoes, estado_inicial, estados_finais):
        """
        Inicializa o autômato finito. M = (Q, Σ, δ, q0, F)
        OBS: Por não ter sido definido um alfabeto na questão ele so irá para no fim da fita (basicamente aceita qualquer simbolo).
        OBS²: Este algoritmo é case sensitive
        
        :param transicoes: Dicionário de transições. Ex: {('q0', 'c'): 'q1', ('q1', 'o'): 'q2'}
        :param estado_inicial: Estado inicial do autômato.
        :param estados_finais: Conjunto de estados finais do autômato.
        """
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
    
    def processa_entrada(self, entrada):
        """
        Processa uma cadeia de entrada e procura por todas as ocorrências da palavra "computador".
        
        :param entrada: Cadeia de entrada a ser processada.
        :return: Lista de índices de início da palavra "computador" se encontrada, caso contrário lista vazia.
        """
        indices = []
        indice_incial = 0
        
        while indice_incial < len(entrada):
            estado_atual = self.estado_inicial
            i = indice_incial
            while i < len(entrada):
                simbolo = entrada[i]
                if (estado_atual, simbolo) in self.transicoes:
                    estado_atual = self.transicoes[(estado_atual, simbolo)]
                    i += 1
                else:
                    break
                if estado_atual in self.estados_finais:
                    indices.append(indice_incial)
                    break
            indice_incial += 1
        
        return indices

if __name__ == "__main__":
    estados_finais = {'q10'}
    transicoes = {
        ('q0', 'c'): 'q1',
        ('q1', 'o'): 'q2',
        ('q2', 'm'): 'q3',
        ('q3', 'p'): 'q4',
        ('q4', 'u'): 'q5',
        ('q5', 't'): 'q6',
        ('q6', 'a'): 'q7',
        ('q7', 'd'): 'q8',
        ('q8', 'o'): 'q9',
        ('q9', 'r'): 'q10',
    }
    estado_inicial = 'q0'
    
    automato = AutomatoFinito(transicoes, estado_inicial, estados_finais)
    
    entradas = [
        "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.",
        "ComputadorcomputadorComputadorComputadorComputadorComputador,computadorcomputadorcomputadorcomputadorcomputadorAAAAAAAAAAcomputador"
    ]
    
    for entrada in entradas:
        print(f"\nTestando a cadeia de entrada: '{entrada}'")
        indices = automato.processa_entrada(entrada)
        if indices:
            print(f"A palavra 'computador' foi encontrada nos índices: {indices}")
        else:
            print("A palavra 'computador' não foi encontrada na cadeia de entrada.")
