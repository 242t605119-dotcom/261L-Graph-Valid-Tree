class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            parent[root_a] = root_b

        return True
