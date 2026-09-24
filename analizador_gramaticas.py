# Script de procesamiento para la determinacion de conjuntos
# de Primeros, Siguientes y Prediccion en gramaticas independientes del contexto.

class ProcesadorGramatica:
    def __init__(self, nombre_gramatica, estructuras_gramatica, simbolo_inicial):
        self.nombre = nombre_gramatica
        self.gramatica = estructuras_gramatica
        self.simbolo_inicial = simbolo_inicial
        
        # Identificacion de simbolos no terminales a partir de la estructura
        self.no_terminales = set(self.gramatica.keys())
        
        # Extraer terminales excluyendo epsilon
        self.terminales = set()
        for producciones in self.gramatica.values():
            for prod in producciones:
                for simbolo in prod:
                    if simbolo not in self.no_terminales and simbolo != 'epsilon':
                        self.terminales.add(simbolo)

        self.primeros = {nt: set() for nt in self.no_terminales}
        self.siguientes = {nt: set() for nt in self.no_terminales}
        self.prediccion = []

    def obtener_primeros_secuencia(self, secuencia):
        # Determina los primeros de una secuencia lineal de simbolos
        resultado = set()
        es_anulable = True

        for simbolo in secuencia:
            if simbolo == 'epsilon':
                continue
            if simbolo in self.terminales:
                resultado.add(simbolo)
                es_anulable = False
                break
            else:
                primeros_no_term = self.primeros[simbolo]
                resultado.update(primeros_no_term - {'epsilon'})
                if 'epsilon' not in primeros_no_term:
                    es_anulable = False
                    break

        if es_anulable:
            resultado.add('epsilon')

        return resultado

    def calcular_conjuntos_primeros(self):
        # Algoritmo de punto fijo iterativo
        hubo_cambio = True
        while hubo_cambio:
            hubo_cambio = False
            for no_term, producciones in self.gramatica.items():
                for prod in producciones:
                    primeros_prod = self.obtener_primeros_secuencia(prod)
                    tamanio_previo = len(self.primeros[no_term])
                    self.primeros[no_term].update(primeros_prod)
                    if len(self.primeros[no_term]) > tamanio_previo:
                        hubo_cambio = True

    def calcular_conjuntos_siguientes(self):
        # Asignar fin de cadena al simbolo inicial
        self.siguientes[self.simbolo_inicial].add('$')

        hubo_cambio = True
        while hubo_cambio:
            hubo_cambio = False
            for no_term, producciones in self.gramatica.items():
                for prod in producciones:
                    for pos, simbolo in enumerate(prod):
                        if simbolo in self.no_terminales:
                            secuencia_restante = prod[pos + 1:]
                            primeros_restante = self.obtener_primeros_secuencia(secuencia_restante)
                            
                            tamanio_previo = len(self.siguientes[simbolo])
                            self.siguientes[simbolo].update(primeros_restante - {'epsilon'})

                            if 'epsilon' in primeros_restante or not secuencia_restante:
                                self.siguientes[simbolo].update(self.siguientes[no_term])

                            if len(self.siguientes[simbolo]) > tamanio_previo:
                                hubo_cambio = True

    def calcular_conjuntos_prediccion(self):
        # Calculo de prediccion por cada regla sintactica
        indice_regla = 1
        for no_term, producciones in self.gramatica.items():
            for prod in producciones:
                primeros_prod = self.obtener_primeros_secuencia(prod)
                conjunto_pred = set()

                if 'epsilon' in primeros_prod:
                    conjunto_pred.update(primeros_prod - {'epsilon'})
                    conjunto_pred.update(self.siguientes[no_term])
                else:
                    conjunto_pred.update(primeros_prod)

                self.prediccion.append((indice_regla, no_term, prod, conjunto_pred))
                indice_regla += 1

    def ejecutar_calculos(self):
        self.calcular_conjuntos_primeros()
        self.calcular_conjuntos_siguientes()
        self.calcular_conjuntos_prediccion()

    def desplegar_reporte(self):
        print(f"\n==========================================")
        print(f"     RESULTADOS PYTHON: {self.nombre}")
        print(f"==========================================")
        
        print("\n--- CONJUNTOS PRIMEROS ---")
        for nt in sorted(self.primeros.keys()):
            elementos = sorted(list(self.primeros[nt]))
            print(f"PRIMEROS({nt}) = {elementos}")

        print("\n--- CONJUNTOS SIGUIENTES ---")
        for nt in sorted(self.siguientes.keys()):
            elementos = sorted(list(self.siguientes[nt]))
            print(f"SIGUIENTES({nt}) = {elementos}")

        print("\n--- CONJUNTOS DE PREDICCION ---")
        for num, nt, prod, pred in self.prediccion:
            regla_str = " ".join(prod)
            pred_ordenado = sorted(list(pred))
            print(f"Regla {num:2d}: {nt} -> {regla_str:<20} | PRED = {pred_ordenado}")


# Definicón de datos de las gramáticas
gramatica_1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['epsilon']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['epsilon']],
    'C': [['cinco', 'D', 'B'], ['epsilon']],
    'D': [['seis'], ['epsilon']]
}

gramatica_2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['epsilon']],
    'B': [['C', 'D'], ['tres'], ['epsilon']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['epsilon']]
}

if __name__ == "__main__":
    proc1 = ProcesadorGramatica("GRAMATICA 1", gramatica_1, 'S')
    proc1.ejecutar_calculos()
    proc1.desplegar_reporte()

    proc2 = ProcesadorGramatica("GRAMATICA 2", gramatica_2, 'S')
    proc2.ejecutar_calculos()
    proc2.desplegar_reporte()
