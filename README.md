# Ilhas de Conectividade

Projeto desenvolvido para a disciplina de **Algoritmos de Alta Performance**.

## 1. Descrição do problema

Dadas `N` cidades e `M` estradas bidirecionais, o objetivo é calcular quantos pares de cidades não possuem caminho entre si. Cidades com um caminho entre elas pertencem ao mesmo componente conexo.

A solução lê `N`, `M` e as extremidades das `M` estradas pela entrada padrão e imprime somente a quantidade de pares desconectados.

## 2. Estratégia: Union-Find (DSU)

A solução utiliza a estrutura de dados Union-Find, também chamada Disjoint Set Union (DSU), para manter os componentes conexos enquanto processa as estradas. Cada cidade começa em seu próprio conjunto. Para cada estrada entre `u` e `v`, a operação `union(u, v)` reúne os conjuntos dessas cidades.

## 3. Operações Find e Union

- **Find:** encontra e retorna a raiz que representa o conjunto de uma cidade.
- **Union:** encontra as raízes de duas cidades e une seus conjuntos se as raízes forem diferentes. A estrutura atualiza o tamanho do conjunto resultante e o número de componentes.

## 4. Otimizações

- **Path Compression:** durante `find`, os elementos visitados passam a apontar diretamente para a raiz. Isso reduz a altura das árvores consultadas.
- **Union by Size:** durante `union`, a árvore do conjunto menor é anexada à raiz do conjunto maior. Assim, a altura das árvores cresce de forma controlada.

As duas otimizações são usadas em conjunto para manter as operações eficientes.

## 5. Escolha da técnica e limites

Os limites são de até 200.000 cidades e 200.000 estradas. A DSU processa cada estrada com operações eficientes de união e percorre as cidades para contar os componentes. Com Path Compression e Union by Size, o custo amortizado por operação é `O(α(N))`, adequado a esses limites sem comparar todos os pares de cidades.

## 6. Cálculo dos pares desconectados

O total de pares distintos de cidades é:

```text
N * (N - 1) / 2
```

Em um componente com `k` cidades, o número de pares conectados é:

```text
k * (k - 1) / 2
```

A solução percorre as cidades de `1` a `N` e considera somente aquelas que são raízes. Para cada raiz, usa o tamanho armazenado na DSU para somar os pares conectados daquele componente. Por fim, calcula:

```text
pares desconectados = total de pares - soma dos pares conectados
```

## 7. Justificativa de corretude

Cada cidade pertence a exatamente um conjunto da DSU. As operações `union` reúnem os conjuntos sempre que uma estrada conecta duas cidades; portanto, ao terminar o processamento, cada conjunto corresponde a um componente conexo da rede.

Componentes diferentes não têm caminho entre si, e todo par de cidades pertence a uma única categoria: ou está no mesmo componente, ou em componentes diferentes. A soma `k * (k - 1) / 2` conta todos os pares dentro de cada componente uma única vez. Subtraindo essa soma do total de pares, restam exatamente os pares que estão em componentes diferentes, isto é, os pares desconectados.

## 8. Complexidade

- **Tempo amortizado:** `O((N + M) * α(N))`, em que `α` é a função inversa de Ackermann.
- **Espaço:** `O(N + M)`, considerando os vetores da DSU e a implementação atual, que lê a entrada inteira de uma vez.

## 9. Testes funcionais

Os testes automatizados em `tests/test_cases.py`, executados com `python -m unittest discover -s tests -v`, verificam inicialização, união, união repetida, conectividade indireta, união por tamanho, elemento isolado e conexão de todos os elementos. Os sete testes passaram.

## 10. Teste de desempenho

O script `tests/performance_test.py` gera uma entrada com 200.000 cidades e 200.000 estradas, executa `src/main.py` como um processo separado e verifica que a saída é `0`. O teste foi aprovado, com tempo medido de aproximadamente **0,374 segundos**.

## Como executar

**Requisito:** Python 3 instalado.

1. Clone o repositório:

```bash
git clone https://github.com/Guilherme-Inacio/ilhas-conectividade.git
```

2. Entre na pasta:

```bash
cd ilhas-conectividade
```

3. Execute o programa:

```bash
python src/main.py
```

4. Informe os dados pela entrada padrão (stdin). Exemplo:

```text
5 2
1 2
3 4
```

Saída esperada:

```text
8
```

**Como executar os testes automatizados:**

```bash
python -m unittest discover -s tests -v
```

Não é necessário instalar bibliotecas externas. O projeto utiliza apenas a biblioteca padrão do Python.

## Tecnologias

- Python 3
- Git e GitHub
- Visual Studio Code

## Estrutura do projeto

```text
ilhas-conectividade/
├── src/
│   └── main.py
├── tests/
│   ├── test_cases.py
│   └── performance_test.py
├── README.md
└── .gitignore
```

## Autores

- Guilherme Inácio Dos Santos Moreira
- Daniel Moraes Delgado
