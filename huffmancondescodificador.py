import heapq
from heapq import heappop, heappush
 
 
def isLeaf(root):
    return root.left is None and root.right is None
 
 
# A Nodo de árbol
class Node:
    def _init_(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right
 
    # Anule la función `_lt_()` para hacer que la clase `Node` funcione con la cola de prioridad
    # tal que el elemento de mayor prioridad tiene la frecuencia más baja
    def _lt_(self, other):
        return self.freq < other.freq
 
 
# Atraviesa el árbol de Huffman y almacena los códigos de Huffman en un diccionario
def encode(root, s, huffman_code):
 
    if root is None:
        return
 
    # encontró un nodo hoja
    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'
 
    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)
 
 
# Atraviesa el árbol de Huffman y decodifica la string codificada
def decode(root, index, s):
 
    if root is None:
        return index
 
    # encontró un nodo hoja
    if isLeaf(root):
        print(root.ch, end='')
        return index
 
    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)
 
 
# Construye Huffman Tree y decodifica el texto de entrada dado
def buildHuffmanTree(text):
 
    # Caso base: string vacía
    if len(text) == 0:
        return
 
    # cuenta la frecuencia de aparición de cada personaje
    # y almacenarlo en un diccionario
    freq = {i: text.count(i) for i in set(text)}
 
    # Crear una cola de prioridad para almacenar nodos activos del árbol de Huffman.
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)
 
    # hacer hasta que haya más de un nodo en la queue
    while len(pq) != 1:
 
        # Eliminar los dos nodos de mayor prioridad
        # (la frecuencia más baja) de la queue
 
        left = heappop(pq)
        right = heappop(pq)
 
        # crea un nuevo nodo interno con estos dos nodos como hijos y
        # con una frecuencia igual a la suma de las frecuencias de los dos nodos.
        # Agregue el nuevo nodo a la cola de prioridad.
 
        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))
 
    # `root` almacena el puntero a la raíz de Huffman Tree
    root = pq[0]
 
    # atraviesa el árbol de Huffman y almacena los códigos de Huffman en un diccionario
    huffmanCode = {}
    encode(root, '', huffmanCode)
 
    # imprime los códigos Huffman
    print('Huffman Codes are:', huffmanCode)
    print('The original string is:', text)
 
    # imprime la string codificada
    s = ''
    for c in text:
        s += huffmanCode.get(c)
 
    print('The encoded string is:', s)
    print('The decoded string is:', end=' ')
 
    if isLeaf(root):
        # Caso especial: Para entradas como a, aa, aaa, etc.
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1
    else:
        # atraviesa el Huffman Tree nuevamente y esta vez,
        # decodifica la string codificada
        index = -1
        while index < len(s) - 1:
            index = decode(root, index, s)
 
 
# Implementación del algoritmo de codificación # Huffman en Python
if __name__ == '_main_':
 
    text = 'Huffman coding is a data compression algorithm.'
    buildHuffmanTree(text)
    