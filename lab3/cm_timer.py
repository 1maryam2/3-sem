import time as t
from contextlib import contextmanager
class cm_timer_1:
    def __enter__(self):
        self.start = t.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit = t.time()
        self.total_time = self.exit - self.start
        print(f'time: {self.total_time:.1f}')
@contextmanager
def cm_timer_2():
    start = t.time()  # Запоминаем время начала
    yield  # Позволяем выполнить блок кода
    exit = t.time()  # Запоминаем время завершения
    total = exit - start  # Вычисляем разницу
    print(f'time: {total:.1f}')  # Выводим результат

with cm_timer_1():
    t.sleep(1)
with cm_timer_2():
    t.sleep(1)