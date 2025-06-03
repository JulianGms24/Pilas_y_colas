from collections import deque

class ColaDeque:
    def __init__(self):
        self.cola = deque()

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.popleft()
        else:
            return "Cola vacía"

    def esta_vacia(self):
        return len(self.cola) == 0

    def tamano(self):
        return len(self.cola)

    def mostrar(self):
        return list(self.cola)

# Prueba
cola = ColaDeque()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Cola actual:", cola.mostrar())
print("Elemento desencolado:", cola.desencolar())
print("Cola después de desencolar:", cola.mostrar())
