from dataclasses import dataclass
import datetime
import re

@dataclass
class Products:
    date: datetime
    product_name: str
    quantity: int

    def __str__(self):
        return f"Дата: {self.date}, Товар: '{self.product_name}', Количество: {self.quantity}"

    @classmethod
    def products_from_string(cls, line: str):
        parts = line.split()
        date_match = re.search(r"\b\d{4}\.\d{2}\.\d{2}\b", line)  # Регулярное выражение
        date = date_match.group() if date_match else None

        quantity_match = re.search(r"(?<!\.)\b([1-9]\d*)\b(?!\.)", line)
        quantity = quantity_match.group() if quantity_match else None

        name_match = re.search(r'"([^"]*)"', line)
        product_name = name_match.group(1).strip() if name_match else None

        return cls(date=date, product_name=product_name, quantity=int(quantity))

def read_file(filename):
    # Используем 'with open', чтобы файл закрылся автоматически
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()  # Считывает все строки из файла и возвращает их в виде списка

def filtered_products(all_products, min_quantity, max_quantity):
    formatted_products = []
    for product in all_products:
        if min_quantity <= int(product.quantity) <= max_quantity:
            formatted_products.append(product)
    return formatted_products

def main():
    filename = "products.txt"

    lines = read_file(filename)  # Читаем данные из файла
    all_products = []

    # Обрабатываем данные
    for line in lines:
        object = Products.products_from_string(line)  # Создаем объект и сразу заполняем его из строки
        all_products.append(object)
        print(object)  # Выводим информацию

    print("1 способ вывести данные товаров, отсортированные по дате")
    print("2 способ вывести данные товаров, отфильтрованные по количеству")
    cnt = int(input("Какой способ вам нужен: "))

    if cnt == 1:
        sorted_by_date = sorted(all_products, key=lambda p: p.date)
        print("Товары, отсортированные по дате:")
        for product in sorted_by_date:
            print(product)

    elif cnt == 2:
        min_quantity = int(input("Введите минимальное количество: "))
        max_quantity = int(input("Введите максимальное количество: "))
        formatted_products = filtered_products(all_products, min_quantity, max_quantity)
        for product in formatted_products:
            print(product)

    else:
        print("Введен неверный способ")

if __name__ == "__main__":
    main()

