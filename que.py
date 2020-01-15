class Queue:

    def __init__(self):  # Kostruktor
        self.Queue = []

    def push(self, s):  # Dodawanie elementów
        self.Queue.append(s)

    def pop(self):  # Usuwanie elementu
        return self.Queue.pop(0)

    def size(self):  # Ilość elementów w kolejce
        return len(self.Queue)

    def empty(self):  # Sprawdza czy kolejka jest pusty
        if len(self.Queue) == 0:
            return True
        else:
            return False
