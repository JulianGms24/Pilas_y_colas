class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            return "Cola vacía"

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)

    def mostrar(self):
        return self.elementos

# Prueba
cola = Cola()
cola.encolar("A")
cola.encolar("B")
cola.encolar("C")
print("Cola actual:", cola.mostrar())
print("Elemento desencolado:", cola.desencolar())
print("Cola después de desencolar:", cola.mostrar())
