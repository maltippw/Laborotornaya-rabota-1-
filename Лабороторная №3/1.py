# TODO Напишите функцию для поиска индекса товара


# Функция для поиска индекса первого вхождения товара в списке
def find_index(items, item_to_find):
    try:
        return items.index(item_to_find)  # Используем метод index()
    except ValueError:
        return None  # Если товар не найден, возвращаем None

# Исходный список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Проверяем несколько товаров
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
