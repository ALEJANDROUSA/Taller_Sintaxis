# Taller: Algoritmos de Primeros, Siguientes y Predicción

## 1. Objetivos de la actividad

- Aplicar las reglas de derivación sintáctica para determinar manualmente los conjuntos de **PRIMEROS**, **SIGUIENTES** y **PREDICCIÓN** de dos gramáticas independientes del contexto.
- Implementar algoritmos basados en el método de **punto fijo** en el lenguaje Python para calcular automáticamente dichos conjuntos.
- Validar la consistencia entre los cálculos teóricos o analíticos y los resultados generados por el script en un entorno Linux, específicamente **Kali Linux**.

---

## 2. Metodología y desarrollo

La actividad se desarrolló mediante las siguientes etapas:

1. **Desarrollo analítico:**  
   Se analizaron las gramáticas identificando los símbolos no terminales anulables, la propagación de símbolos iniciales mediante los conjuntos de **PRIMEROS** y la herencia de contexto mediante los conjuntos de **SIGUIENTES** y **PREDICCIÓN**.

2. **Implementación del algoritmo:**  
   Se estructuró una clase en Python denominada `ProcesadorGramatica`, encargada de procesar arreglos de reglas sintácticas y ejecutar tres ciclos de punto fijo hasta alcanzar la convergencia de los conjuntos calculados.

3. **Verificación y comparación:**  
   Se compararon los resultados obtenidos manualmente con las salidas generadas por el programa, verificando la coincidencia de los conjuntos de PRIMEROS, SIGUIENTES y PREDICCIÓN.

---

## 3. Tecnologías utilizadas

- **Lenguaje de programación:** Python 3.
- **Sistema operativo:** Kali Linux.
- **Editor de texto:** Nano.
- **Método algorítmico:** Punto fijo.
- **Tema:** Análisis sintáctico de gramáticas independientes del contexto.

---

## 4. Comandos utilizados en Kali Linux

### 4.1. Creación del espacio de trabajo

```bash
mkdir -p ~/Taller_Sintaxis
cd ~/Taller_Sintaxis
```

### 4.2. Creación del archivo de código

```bash
nano analizador_gramaticas.py
```

En este archivo se implementa la clase `ProcesadorGramatica`, que permite calcular los conjuntos de PRIMEROS, SIGUIENTES y PREDICCIÓN para las gramáticas analizadas.

### 4.3. Ejecución del programa

```bash
python3 analizador_gramaticas.py
```

---

## 5. Capturas de pantalla de la ejecución

<img width="1600" height="1307" alt="image" src="https://github.com/user-attachments/assets/b6ea1dd3-5d22-4be5-9108-cdbaf294d7ff" />


### 5.2. Resultados algorítmicos de la gramática 2

<img width="1600" height="1153" alt="image" src="https://github.com/user-attachments/assets/36fe3bbe-83c4-4517-ad80-9b651d269a47" />


## 6. Tabla comparativa de resultados

| Gramática | Componente | Resultado analítico (manual) | Resultado del script (Python) | ¿Coinciden? |
|---|---|---|---|---|
| Gramática 1 | PRIMEROS(S) | `{uno, tres, cuatro, cinco, seis}` | `['cuatro', 'cinco', 'cuatro', 'seis', 'tres', 'uno']` | Sí |
| Gramática 1 | SIGUIENTES(S) | `{$, dos}` | `['$', 'dos']` | Sí |
| Gramática 1 | PRED(R1) | `{uno, tres, cuatro, cinco, seis}` | `['cuatro', 'cinco', 'seis', 'tres', 'uno']` | Sí |
| Gramática 2 | PRIMEROS(S) | `{uno, dos, tres, cuatro, cinco}` | `['dos', 'tres', 'cuatro', 'cinco', 'uno']` | Sí |
| Gramática 2 | SIGUIENTES(A) | `{uno, tres, cuatro, cinco, seis}` | `['cuatro', 'cinco', 'seis', 'tres', 'uno']` | Sí |
| Gramática 2 | PRED(R1) | `{uno, dos, tres, cuatro, cinco}` | `['dos', 'tres', 'cuatro', 'cinco', 'uno']` | Sí |

> **Nota:** El orden de los elementos en las listas generadas por Python puede variar, ya que los conjuntos no necesariamente conservan un orden específico. La comparación se realiza considerando los elementos que pertenecen a cada conjunto.

---

## 7. Análisis de resultados

A partir de la comparación entre los resultados manuales y los resultados generados por el programa, se observó que los conjuntos calculados coinciden en todos los casos analizados.

La implementación basada en el método de punto fijo permitió automatizar el cálculo de los conjuntos sintácticos y comprobar los resultados obtenidos mediante el procedimiento teórico.

Los resultados muestran coincidencia en:

- Los conjuntos de **PRIMEROS** de ambas gramáticas.
- Los conjuntos de **SIGUIENTES** analizados.
- Los conjuntos de **PREDICCIÓN** de las reglas evaluadas.

---

## 8. Conclusión

Se comprobó una coincidencia del **100 %** entre los cálculos manuales y la simulación algorítmica realizada mediante Python.

Además, se determinó que ambas gramáticas analizadas presentan conflictos en sus conjuntos de **PREDICCIÓN**. Por esta razón, de acuerdo con el análisis realizado, **ninguna de las dos gramáticas cumple con el criterio LL(1)**.

La actividad permitió reforzar el conocimiento de los conjuntos de PRIMEROS, SIGUIENTES y PREDICCIÓN, así como comprender la utilidad del método de punto fijo para automatizar el análisis sintáctico de gramáticas independientes del contexto.

---

## 9. Estructura del proyecto

```text
Taller_Sintaxis/
│
└── analizador_gramaticas.py
```

---

## 10. Requisitos de ejecución

Para ejecutar el proyecto se requiere:

1. Tener instalado Python 3.
2. Contar con un entorno Linux, como Kali Linux.
3. Guardar el código en el archivo `analizador_gramaticas.py`.
4. Ejecutar el programa mediante el comando:

```bash
python3 analizador_gramaticas.py
```

---

## 11. Resultado final

El programa permite calcular automáticamente los conjuntos de PRIMEROS, SIGUIENTES y PREDICCIÓN, facilitando la comparación entre el procedimiento manual y el procedimiento algorítmico.

Los resultados obtenidos permiten concluir que existe consistencia entre el análisis teórico y la implementación en Python, aunque las gramáticas estudiadas presentan conflictos que impiden clasificarlas como gramáticas LL(1).
