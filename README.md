# Analizador de Polinomios con AFD

Herramienta web que valida polinomios simples (variable x) usando un Autómata Finito Determinista (AFD) y genera tokens léxicos.

## Características
- ✅ Validación estructural mediante AFD
- 🔍 Lexer atómico (números, variable, operadores, potencia)
- 🌙 Modo oscuro/claro con persistencia
- 🎯 Resaltado exacto de errores
- 📊 Diagrama interactivo del AFD (Mermaid.js)

## Uso
1. Escribe un polinomio en el campo de texto
2. Haz clic en "Analizar"
3. Verás si es válido y la lista de tokens generados

## Ejemplos válidos
- `3x^2 - 5x + 2`
- `-x^10 + 1`
- `7`

## Tecnologías
- HTML5, CSS3, JavaScript (ES6)
- Mermaid.js para diagramas
- Desplegado en GitHub Pages

## Enlace
[Ver herramienta en vivo](https://wil-1302.github.io/polinomios/)
