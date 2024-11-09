# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def index_finder(list_arg, item_to_search):
    for index, item in enumerate(list_arg):
        if item == item_to_search:
            return index
    return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = index_finder(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
