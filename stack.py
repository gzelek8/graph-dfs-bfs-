class Stack:

    def __init__(self):  # Kostruktor
        self.Stack = []

    def push(self, s):  # Dodawanie elementów
        self.Stack.append(s)

    def pop(self):  # Usuwanie elementu
        self.Stack.pop(len(self.Stack) - 1)

    def size(self):  # Ilość elementów na stosie
        return len(self.Stack)

    def top(self):  # Zwraca ostatni element
        return self.Stack[len(self.Stack) - 1]

    def empty(self):  # Sprawdza czy stos jest pusty
        if len(self.Stack) == 0:
            return True
        else:
            return False
