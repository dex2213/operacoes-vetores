# 🔢 Operações com Vetores em Python

Projeto que demonstra operações matemáticas elemento a elemento entre dois vetores, evoluindo de uma implementação manual com Python puro até uma versão otimizada com **NumPy**.

---

## 📌 Sobre o Projeto

Este repositório mostra a evolução de um mesmo problema resolvido de duas formas:

- **Versão 1** — Python puro, com lógica manual usando `for` e `zip`
- **Versão 2** — Python com NumPy, mais eficiente, limpa e com estatísticas automáticas

O objetivo é entender o conceito fundamental por baixo de bibliotecas como NumPy, que é amplamente usada em ciência de dados, finanças, redes e muito mais.

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x instalado
- Para a versão NumPy: `pip install numpy`

### Executando

```bash
# Versão Python puro
python vetores_puro.py

# Versão NumPy
python vetores_numpy.py
```

### Exemplo de entrada

```
Primeiro vetor, separe com ',' :  10, 20, 30, 40
Segundo vetor, separe com ',' :   5, 10, 15, 20
Escolha a operação (+, -, *, /): -
```

### Saída esperada

```
Primeiro vetor: [10, 20, 30, 40]
Segundo vetor:  [ 5, 10, 15, 20]
Resultado (-):  [ 5, 10, 15, 20]

📊 Estatísticas do resultado:
  Soma:   50
  Média:  12.50
  Maior:  20
  Menor:  5
```

---

## 📁 Estrutura do Repositório

```
operacoes-vetores/
│
├── vetores_puro.py       # Versão com Python puro
├── vetores_numpy.py      # Versão otimizada com NumPy
└── README.md             # Documentação do projeto
```

---

## 🔍 Comparação entre as Versões

| Característica         | Python Puro         | NumPy                        |
|------------------------|---------------------|------------------------------|
| Operações              | Loop manual         | Operação direta no array     |
| Divisão por zero       | Erro manual         | Proteção automática          |
| Estatísticas           | Não incluído        | sum, mean, max, min          |
| Performance            | Adequada para pouco dados | Escalável para milhões  |
| Linhas de código       | ~25 linhas          | ~20 linhas                   |

---

## 💡 Casos de Uso Reais

- **Redes:** comparar largura de banda contratada vs consumida em múltiplos links
- **Finanças:** calcular variação de preços entre dois períodos
- **Varejo:** apurar lucro unitário de vários produtos de uma vez
- **Educação:** calcular média ponderada de uma turma inteira
- **IoT / Sensores:** somar ou comparar leituras de múltiplos sensores simultaneamente

---

## 📚 O que Aprendi

- Manipulação de listas e arrays em Python
- Uso de `zip()` para iterar dois vetores em paralelo
- Introdução ao NumPy: arrays, operações vetorizadas e funções estatísticas
- Tratamento de erros (divisão por zero, tamanhos diferentes)
- Boas práticas de organização de código com dicionários

---

## 👨‍💻 Autor

**Andre Ferreira**  
Estudante de Ciências da Computação — GRAN Faculdade  
[LinkedIn](https://www.linkedin.com/in/andreferreira-26070434a)

---

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar e modificar.
