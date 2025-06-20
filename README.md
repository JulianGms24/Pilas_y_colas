# Pilas y Colas - Ejercicios en Python

Este proyecto contiene la implementación básica de estructuras de datos tipo **cola**, utilizando listas y `deque` de la biblioteca estándar de Python. Es parte del estudio de estructuras de información.

## 📘 Contenido

### ✅ Ejercicio 1: Cola con lista
Se implementa una cola utilizando una lista (`list`) de Python. Se incluyen los siguientes métodos:

- `encolar(elemento)`: agrega un elemento al final de la cola.
- `desencolar()`: elimina y retorna el primer elemento de la cola.
- `esta_vacia()`: verifica si la cola está vacía.
- `tamano()`: retorna la cantidad de elementos en la cola.
- `mostrar()`: muestra los elementos actuales de la cola.

**Prueba incluida:**  
Se encolan tres elementos ("A", "B", "C"), se muestra la cola, se desencola uno y se vuelve a mostrar el estado.

---

### ✅ Ejercicio 2: Cola con `deque`
En este ejercicio se utiliza la estructura `deque` del módulo `collections`, optimizada para inserciones y eliminaciones en ambos extremos.

Métodos implementados:

- `encolar(elemento)`: agrega al final de la cola.
- `desencolar()`: elimina y retorna el primer elemento.
- `esta_vacia()`: verifica si la cola está vacía.
- `tamano()`: retorna la cantidad de elementos.
- `mostrar()`: convierte el `deque` en lista para mostrarla.

**Prueba incluida:**  
Se encolan los enteros 1, 2 y 3. Luego se desencola uno y se muestra la cola antes y después.

---

## 🚀 Requisitos

- Python 3.x

## ▶️ Cómo ejecutar

Desde la terminal o PowerShell:

```bash
python ejercicio1.py
python ejercicio2.py
