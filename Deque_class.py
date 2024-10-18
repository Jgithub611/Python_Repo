class Deque:
    def __init__(self):
        self.__deque=[]

    def add_first(self,item):
        self.__deque.insert(0,item)

    def is_empty(self):
        return len(self.__deque)==0

    def remove_first(self):
        if self.is_empty():
            print("No hay elementos que eliminar")
        else:self.__deque.pop(0)

    def add_last(self,item):
        self.__deque.append(item)

    def remove_last(self):
        if self.is_empty():
            print("No hay elementos que eliminar")
        else:self.__deque.pop()

    def __str__(self):
        return f"{self.__deque}"

    def peek_front(self):
        print(f"El primer elemento es: {self.__deque[0]}")

    def peek_last(self):
        print(f"El último elemento es: {self.__deque[-1]}")

    def remove_all(self):
        if self.is_empty():
            print("No hay elementos que eliminar")
        else:self.__deque.clear()


Deque=Deque()

Deque.add_first(12)
Deque.add_last(30)
Deque.add_first(15)
print(Deque)
Deque.remove_first()
Deque.remove_last()
print(Deque)
Deque.add_first(54)
Deque.add_last(30)
print(Deque)
Deque.peek_front()
Deque.peek_last()
Deque.remove_all()
print(Deque)
Deque.remove_first()
Deque.remove_last()