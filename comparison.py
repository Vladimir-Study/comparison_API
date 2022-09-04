import json
from pprint import pprint


class ComparisonAPI():

    # метод работы аналитикой 
    def get_analitic_ozon(self):
        pass

    # метод получения заказов озон
    def get_orders_ozon(self):
        pass

    # метод получения заказов яндекс
    def get_orders_yandex(self):
        pass
    
    # метод сохранения в файл csv
    def record_csv(self):
        pass

    # и т.д.


with open('comparison.json', 'r', encoding='utf-8') as file:
    comparison = json.load(file)
    # получение первого(родительского) метода
    parent = 'get_analitic_ozon'
    # получение второго(дочернего) метода
    successor = 'record_csv'
    test_comparison = ComparisonAPI
    for line in comparison:
        for key, val in line.items():
            if key == parent and successor in val:
                if hasattr(test_comparison, parent) and hasattr(test_comparison, successor):
                    # Вызываем поочередно методы класса к выполнению
                    print(True)
