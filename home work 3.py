text = "Вивчаємо мову програмування Python разом"
words = text.split()
for index, word in enumerate(words, start=1):
    print(f"{index}. {word}")

items = ["яблуко", "банан", "яблуко", "груша", "банан", "слива"]
unique_items = []
first_indices = []
for index, item in enumerate(items):
    if item not in unique_items:
        unique_items.append(item)
        first_indices.append(index)
print("Унікальні елементи:", unique_items)
print("Індекси перших входжень:", first_indices)

continents = ["Північна Америка", "Південна Америка"]
eastern_continents = ["Євразія", "Африка", "Австралія", "Антарктида"]
continents.extend(eastern_continents)
continents.sort()
print("Усі материки за алфавітом:", continents)

students = [
    ["Андрій", "Коваленко"],
    ["Олена", "Шевченко"],
    ["Андрій", "Бондаренко"],
    ["Марія", "Ткаченко"],
    ["Андрій", "Мельник"]
]
andriy_count = 0
for student in students:
    if student[0] == "Андрій":
        andriy_count += 1
print(f"Кількість студентів з іменем Андрій: {andriy_count}")
