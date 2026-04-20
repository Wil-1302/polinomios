# Definición de Estados
Q0 = "INICIO"
Q1 = "SIGNO"
Q2 = "COEFICIENTE"
Q3 = "VARIABLE"
Q4 = "POTENCIA"
Q5 = "EXPONENTE"
QE = "ERROR"

def transicion(estado, caracter):
    if caracter == ' ':
        return estado
    if caracter.isdigit():
        if estado in [Q0, Q1, Q2]:
            return Q2
        if estado in [Q4, Q5]:
            return Q5
        return QE
    if caracter in ['+', '-']:
        if estado in [Q0, Q2, Q3, Q5]:
            return Q1
        return QE
    if caracter == 'x':
        if estado in [Q0, Q1, Q2]:
            return Q3
        return QE
    if caracter == '^':
        if estado == Q3:
            return Q4
        return QE
    return QE

def es_aceptacion(estado):
    return estado in [Q2, Q3, Q5]

def validar_polinomio_simple(cadena):
    estado_actual = Q0
    for caracter in cadena:
        estado_actual = transicion(estado_actual, caracter)
        if estado_actual == QE:
            return False
    return es_aceptacion(estado_actual)

if __name__ == "__main__":
    tests = [
        "3x^2 - 5x + 2",
        "x",
        "-7",
        "+x^10",
        "3x^",
        "5x^^2",
        "4x - +2",
        "3x 5"
    ]
    for t in tests:
        resultado = "VÁLIDO" if validar_polinomio_simple(t) else "INVÁLIDO"
        print(f"'{t}': {resultado}")
