from pprint import pprint
import os


file_name = 'Recipe.txt'


def convert_file_to_dict(file: str) -> dict:
    recipes_dict = {}

    with open(file, encoding='utf-8') as recipe:
        for line in recipe:
            ingredient = []
            dish = line.strip()
            recipes_dict.setdefault(dish)
            quantity = recipe.readline()
            for ingredients in range(int(quantity)):
                key_name = ['ingredient_name', 'quantity', 'measure']
                ingredient.append(dict(zip(key_name, recipe.readline().strip().split('|'))))
            recipes_dict[dish] = ingredient
            recipe.readline()

    return recipes_dict


cook_book = convert_file_to_dict(file_name)

pprint(cook_book, width=120, sort_dicts=False)
print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_lst = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingr in ingredients:
                ingredient = ingr['ingredient_name']
                products = int(ingr['quantity']) * person_count
                measure = ingr['measure']
                if ingredient in shop_lst:
                    shop_lst[ingredient]['quantity'] += products
                else:
                    prod_dict = dict(zip(['measure', 'quantity'], [measure, products]))
                    shop_lst.setdefault(ingredient, prod_dict)

    return shop_lst


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

pprint(shop_list, sort_dicts=False)


def number_of_line(*files):
    text_dict = {}
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            lines = len(file_obj.readlines())
            text_dict.setdefault(file, lines)

    sorted_text_keys = sorted(text_dict, key=text_dict.get)
    sorted_text_dict = {}
    for fl in sorted_text_keys:
        sorted_text_dict[fl] = text_dict[fl]

    return sorted_text_dict


def writing_file(dictionary):

    base_path = os.getcwd()
    text_name = 'text.txt'

    full_path = os.path.join(base_path, text_name)
    text = {}
    for key, value in dictionary.items():
        with open(key, encoding='utf-8') as file_obj:
            text.setdefault(key, file_obj.read().strip())

    with open(full_path, 'a', encoding='utf-8') as new_file:
        for key, value in text.items():
            new_file.write(f'{key}\n')
            new_file.write(f'{str(dictionary[key])}\n')
            new_file.write(f'{value}\n')


number_line = number_of_line('file1.txt', 'file2.txt', 'file3.txt')

writing_file(number_line)
