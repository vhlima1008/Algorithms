from __future__ import annotations
from typing import Optional, List

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        
class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None
        
    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)
        
    def _insert(self, node: Optional[Node], key: int):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    
    
    
    # --------- PRETTY PRINT (top-down like your image) ---------
    def traverse_print(self) -> None:
        """Imprime a árvore no console (top-down com _ e / \\)."""
        if self.root is None:
            print("(empty)")
            return

        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line.rstrip())

    def _display_aux(self, node: Node):
        """
        Retorna (lines, width, height, middle)
        lines: lista de strings (cada string é uma linha do desenho)
        """
        s = str(node.key)
        u = len(s)

        # Caso 1: sem filhos
        if node.left is None and node.right is None:
            return [s], u, 1, u // 2

        # Caso 2: só filho esquerdo
        if node.right is None:
            left_lines, n, p, x = self._display_aux(node.left)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in left_lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + (u // 2)

        # Caso 3: só filho direito
        if node.left is None:
            right_lines, n, p, x = self._display_aux(node.right)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in right_lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Caso 4: dois filhos
        left_lines, n, p, x = self._display_aux(node.left)
        right_lines, m, q, y = self._display_aux(node.right)

        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "

        # normaliza alturas
        if p < q:
            left_lines += [" " * n] * (q - p)
        elif q < p:
            right_lines += [" " * m] * (p - q)

        lines = [a + u * " " + b for a, b in zip(left_lines, right_lines)]
        return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + (u // 2)
        
bst = BinarySearchTree()
for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(x)

bst.traverse_print()
