NUMERO    = 'NUMERO'
VARIABLE  = 'VARIABLE'
POTENCIA  = 'POTENCIA'
SUMA      = 'SUMA'
RESTA     = 'RESTA'
ERROR     = 'ERROR'
EOF       = 'EOF'

class Lexer:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0
        self.actual = texto[0] if texto else ''
    
    def avanzar(self):
        self.pos += 1
        self.actual = self.texto[self.pos] if self.pos < len(self.texto) else ''
    
    def ignorar_espacios(self):
        while self.actual == ' ':
            self.avanzar()
    
    def leer_numero(self):
        inicio = self.pos
        while self.actual.isdigit():
            self.avanzar()
        return (NUMERO, self.texto[inicio:self.pos], inicio)
    
    def siguiente_token(self):
        self.ignorar_espacios()
        
        if self.pos >= len(self.texto):
            return (EOF, '', self.pos)
            
        if self.actual.isdigit():
            return self.leer_numero()
            
        if self.actual == 'x':
            token = (VARIABLE, 'x', self.pos)
            self.avanzar()
            return token
            
        if self.actual == '^':
            token = (POTENCIA, '^', self.pos)
            self.avanzar()
            return token
            
        if self.actual == '+':
            token = (SUMA, '+', self.pos)
            self.avanzar()
            return token
            
        if self.actual == '-':
            token = (RESTA, '-', self.pos)
            self.avanzar()
            return token
            
        # Error
        token = (ERROR, self.actual, self.pos)
        self.avanzar()
        return token
    
    def tokenizar(self):
        tokens = []
        while True:
            tok = self.siguiente_token()
            tokens.append(tok)
            if tok[0] in (EOF, ERROR):
                break
        return tokens

def tokenizar(cadena: str) -> list:
    lex = Lexer(cadena)
    return lex.tokenizar()

if __name__ == '__main__':
    pruebas = [
        "3x^2 - 5x + 1",
        "10x - 7",
        "4x @ 2"
    ]
    
    for i, entrada in enumerate(pruebas, 1):
        print(f"\n--- Prueba {i}: '{entrada}' ---")
        tokens = tokenizar(entrada)
        for t in tokens:
            print(t)
