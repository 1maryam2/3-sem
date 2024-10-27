from collections import defaultdict
class Manufacturer:
    def __init__(self, manufacturer_id, name):
        self.manufacturer_id = manufacturer_id
        self.name = name

class Part:
    def __init__(self, part_id, name, manufacturer_id):
        self.part_id = part_id
        self.name = name
        self.manufacturer_id = manufacturer_id

class ManufacturerEmployee:
    def __init__(self, employee_id, manufacturer_id):
        self.employee_id = employee_id
        self.manufacturer_id = manufacturer_id

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

# Список производителей
manufacturers = [
    Manufacturer(1, "Кировский завод"),
    Manufacturer(2, "Технопром"),
    Manufacturer(3, "КамАЗ"),
    Manufacturer(4, "Автопром")
]

# Список деталей
parts = [
    Part(1, "Мотор", 1),
    Part(2, "Ротор", 2),
    Part(3, "Амортизатор", 3),
    Part(4, "Генератор", 1),
    Part(5, "Транзистор", 2)
]

# Список сотрудников
employees = [
    Employee(1, "Алексей"),
    Employee(2, "Борис"),
    Employee(3, "Кирилл"),
    Employee(4, "Дмитрий"),
    Employee(5, "Евгений")
]

# Список соответствий сотрудники-производители (для связи многие-ко-многим)
manufacturer_employees = [
    ManufacturerEmployee(1, 1),
    ManufacturerEmployee(2, 2),
    ManufacturerEmployee(3, 3),
    ManufacturerEmployee(4, 1),
    ManufacturerEmployee(5, 3)
]

result1 = [
    (part.name, manufacturer.name)
    for part in parts
    for manufacturer in manufacturers
    if part.manufacturer_id == manufacturer.manufacturer_id and part.name.endswith("ор")
]

print("1)Детали, заканчивающиеся на 'ор', и их производители:")
for part_name, manufacturer_name in result1:
    print(f"Деталь: {part_name}, Производитель: {manufacturer_name}")

# Подсчет количества деталей у каждого производителя
manufacturer_parts_count = defaultdict(int)
for part in parts:
    manufacturer_parts_count[part.manufacturer_id] += 1

# Подсчет среднего количества производимых деталей
manufacturer_avg_parts = [
    (manufacturer.name, manufacturer_parts_count[manufacturer.manufacturer_id])
    for manufacturer in manufacturers
]

# Сортировка производителей по среднему количеству деталей
manufacturer_avg_parts_sorted = sorted(manufacturer_avg_parts, key=lambda x: x[1], reverse=True)

print("2)Производители и среднее количество производимых деталей:")
for manufacturer_name, avg_part_count in manufacturer_avg_parts_sorted:
    print(f"Производитель: {manufacturer_name}, Среднее количество деталей: {avg_part_count}")

result3 = [
    (manufacturer.name, [employee.name for employee in employees if any(me.employee_id == employee.employee_id and me.manufacturer_id == manufacturer.manufacturer_id for me in manufacturer_employees)])
    for manufacturer in manufacturers
    if manufacturer.name.startswith("К")
]

print("3)Производители, начинающиеся с 'К', и их сотрудники:")
for manufacturer_name, employee_names in result3:
    print(f"Производитель: {manufacturer_name}, Сотрудники: {', '.join(employee_names)}")
