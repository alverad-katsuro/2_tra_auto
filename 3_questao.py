class TransdutorMealy:
    def __init__(self, estados, alfabeto, alfabeto_transdutor, transicoes, funcao_transducao, estado_inicial, estados_finais):
        """
        Inicializa o autômato finito. TMealy = (Q, Σ, ∆, δ, λ, q0, F)

        :param estados: Conjunto de estados do autômato.
        :param alfabeto: Conjunto de símbolos do alfabeto do autômato.
        :param alfabeto_transdutor: Conjunto de símbolos do alfabeto do transdutor.
        :param transicoes: Dicionário de transições. Ex: {('q0', 'a'): 'q1', ('q0', 'b'): 'q2'}
        :param funcao_transducao: Dicionário de transdução. Ex: {('q0', 'a'): 'q1', ('q0', 'b'): 'q2'}
        :param estado_inicial: Estado inicial do autômato.
        :param estados_finais: Conjunto de estados finais do autômato.
        """
        
        self.estados = estados
        self.alfabeto = alfabeto
        self.alfabeto_transdutor = alfabeto_transdutor
        self.transicoes = transicoes
        self.funcao_transducao = funcao_transducao
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.estado_atual = estado_inicial

    def reset(self):
        """ Reinicia o estado atual para o estado inicial. """
        self.estado_atual = self.estado_inicial

    def step(self, simbolo_entrada):
        """
        Executa um passo do transdutor dado um símbolo de entrada.

        :param simbolo_entrada: Símbolo de entrada a ser processado.
        :return: Símbolo de saída correspondente ao símbolo de entrada.
        """
        if self.estado_atual not in self.transicoes or simbolo_entrada not in self.transicoes[self.estado_atual]:
            raise ValueError(f"Nenhuma transição definida para o estado {self.estado_atual} com a entrada {simbolo_entrada}")

        proximo_estado = self.transicoes[self.estado_atual][simbolo_entrada]
        simbolo_saida = self.funcao_transducao[self.estado_atual][simbolo_entrada]
        self.estado_atual = proximo_estado
        return simbolo_saida

    def run(self, entrada):
        """
        Executa o transdutor em uma lista de entrada de símbolos.

        :param entrada: Lista de entrada de símbolos a ser processada.
        :return: String de saída resultante da transdução.
        """
        self.reset()
        string_saida = []
        for simbolo in entrada:
            simbolo_saida = self.step(simbolo)
            string_saida.append(simbolo_saida)
        return string_saida




if __name__ == "__main__":
    estados = {'q0', 'q1','q2','q3'}
    alfabeto = {25, 50,100}
    alfabeto_transdutor = {0,1}
    transicoes = {
        'q0': {100: 'q0', 25: 'q1', 50: 'q2'},
        'q1': {100: 'q1', 25: 'q2', 50: 'q3'},
        'q2': {100: 'q2', 25: 'q3', 50: 'q0'}, 
        'q3': {100: 'q3', 50: 'q1', 25: 'q0'},
    }
    funcao_transducao = {
        'q0': {100: 1, 25: 0, 50: 0}, # 0c
        'q1': {100: 1, 25: 0, 50: 0}, # 25c
        'q2': {100: 1, 25: 0, 50: 1}, # 50c
        'q3': {100: 1, 25: 1, 50: 1}, # 75c
    }
    estado_inicial = 'q0'
    estados_finais = {'q0','q1','q2','q3'}

    mealy = TransdutorMealy(estados, alfabeto, alfabeto_transdutor, transicoes, funcao_transducao, estado_inicial, estados_finais)

    entrada = [50,25,50,100,25,50,100,100,100,100,25,25,25,25,50,50]
    string_saida = mealy.run(entrada)
    print(f"Entrada: {entrada}\nSaída: {string_saida}")