class UnionFind:
    def __init__(self, n):
        # O índice 0 fica reservado; os elementos válidos vão de 1 até n.
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n

    def find(self, x):
        # Percorre até a raiz e comprime o caminho durante o retorno.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        # Não há mudança quando os elementos já estão no mesmo conjunto.
        if root_a == root_b:
            return

        # Mantém a árvore menor como filha da árvore maior.
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.components -= 1
