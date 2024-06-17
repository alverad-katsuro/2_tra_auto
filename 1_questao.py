class AutomatoFinito:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        """
        Inicializa o automato finito. M = (Q, Σ, δ, q0, F)

        :param estados: Conjunto de estados do automato.
        :param alfabeto: Conjunto de símbolos do alfabeto do automato.
        :param transicoes: Dicionário de transições. Ex: {('q0', 'a'): 'q1', ('q0', 'b'): 'q2'}
        :param estado_inicial: Estado inicial do automato.
        :param estados_finais: Conjunto de estados finais do automato.
        """
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def processa_entrada(self, entrada):
        """
        Processa uma cadeia de entrada e verifica se ela é aceita pelo automato.

        :param entrada: Cadeia de entrada a ser processada.
        :return: True se a cadeia é aceita, False caso contrário.
        """
        estado_atual = self.estado_inicial

        for simbolo in entrada:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
            else:
                return False

        return estado_atual in self.estados_finais


def prim1a():
    estados = {'q0', 'q1', 'q2', 'q3'}
    alfabeto = {'a', 'b','c'}
    transicoes = {
        ('q0', 'a'): 'q1',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q3',
        ('q2', 'a'): 'q1',
        ('q2', 'b'): 'q2',
        ('q2', 'c'): 'q3',
        ('q3', 'a'): 'q1',
        ('q3', 'c'): 'q3',
    }
    estado_inicial = 'q0'
    estados_finais = {'q0','q1','q2','q3'}

    automato = AutomatoFinito(estados, alfabeto, transicoes, estado_inicial, estados_finais)
    
    entradas = ['','a','aaaaaaaaaaaaaaaaaaaa','abc','ab','ac','accccccccccc','abbbbbbcccccccccccc','abbbbbbaaaaccc','abbbbbbccccccccccccabbbbbbccccccccccccabbbbbbcccccccccccc','bc','c','b','cb','cbcbcbcbcb','bbbbbbbbbbbbbbbb','cccccccccccccc','bccccccccc','cbbbbbbbbbbbbbb','bcaa']
    for entrada in entradas:
        resultado = automato.processa_entrada(entrada)
        print(f"A entrada '{entrada}' é {'aceita' if resultado else 'rejeitada'} pelo automato.")

def prim1b():
    estados = {'q0', 'q1q6', 'q2q7', 'q3q8','q4','q5','q6','q7','q8'}
    alfabeto = {'a', 'b','c'}
    transicoes = {
        ('q0', 'a'): 'q1q6',
        ('q0', 'b'): 'q5',
        ('q0', 'c'): 'q5',
        ('q1q6', 'a'): 'q2q7',
        ('q2q7', 'a'): 'q3q8',
        ('q3q8', 'b'): 'q4',
        ('q3q8', 'c'): 'q4',
        ('q4', 'b'): 'q4',
        ('q4', 'c'): 'q4',
        ('q5', 'b'): 'q5',
        ('q5', 'c'): 'q5',
        ('q5', 'a'): 'q6',
        ('q6', 'a'): 'q7',
        ('q7', 'a'): 'q8',
    }
    estado_inicial = 'q0'
    estados_finais = {'q3q8','q4','q8'}

    automato = AutomatoFinito(estados, alfabeto, transicoes, estado_inicial, estados_finais)
    
    entradas = ['aaa','aaabbbbbbbbbbbbb','aaabbbbbcccccccccc','aaab','aaac','aaabbbbccccbcbcbcbbcbcbcbcbc','aaacbcbcbcbcb','bcbcbcbcbcaaa','cccccccaaa','bbbbbbbbccccccaaa','bbbbbbbbbbbb','ccccccccccc','bccccbbb','aa','a','abc','acb','','aaaaaabccc','aaaaabbbccc']
    for entrada in entradas:
        resultado = automato.processa_entrada(entrada)
        print(f"A entrada '{entrada}' é {'aceita' if resultado else 'rejeitada'} pelo automato.")

def prim1c():
    estados = {'q0', 'q1', 'q2', 'q3','q4', 'q5'}
    alfabeto = {'a', 'b'}
    transicoes = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q5',
        ('q1', 'a'): 'q3',
        ('q1', 'b'): 'q2',
        ('q2', 'b'): 'q2',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q4',
    }
    estado_inicial = 'q0'
    estados_finais = {'q1','q2','q4','q5'}

    automato = AutomatoFinito(estados, alfabeto, transicoes, estado_inicial, estados_finais)
    
    entradas = ['b','a','ab','aab','abb','aaaaab','aaaaaaaaaaaaaaaaaaab','aaaaaab','abbbbbbbbbbbbbbbb','','aaaaaaaaabbbbbbbbb','ba','bbbbbaaaaaaa','bbbbbbb','aaaaaaaaa','babababa','baaaaaaaa','abababab','bbbbbbaaaaa','aaabbb','avx']
    for entrada in entradas:
        resultado = automato.processa_entrada(entrada)
        print(f"A entrada '{entrada}' é {'aceita' if resultado else 'rejeitada'} pelo automato.")

def prim1d():
    estados = {'q0', 'q1', 'q2', 'q3','q4'}
    alfabeto = {'a', 'b','c'}
    transicoes = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q2',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q4',
        ('q2', 'b'): 'q2',
        ('q2', 'a'): 'q3',
        ('q3', 'c'): 'q4',
        ('q4', 'c'): 'q4',
    }
    estado_inicial = 'q0'
    estados_finais = {'q1','q3','q4'}

    automato = AutomatoFinito(estados, alfabeto, transicoes, estado_inicial, estados_finais)
    
    entradas = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccc','a','ac','aba','abbbba','ba','bac','bbbbbaccccccc','abac','abbbbbbbbbac','abbbbbbbbbbbbacccccccccc','','cccccccc','bbbbbbbbbbb','abacca','abaaaaaaaaa','cac','xxxxxb']
    for entrada in entradas:
        resultado = automato.processa_entrada(entrada)
        print(f"A entrada '{entrada}' é {'aceita' if resultado else 'rejeitada'} pelo automato.")

if __name__ == "__main__":
    print("1. a)")
    prim1a()
    print("1. b)")
    prim1b()
    print("1. c)")
    prim1c()
    print("1. d)")
    prim1d()