with open('recipes.txt', encoding='utf8') as f:
    cook_book = {}
    for line in f:
        name_dish = line.strip()
        hm_dish = int(f.readline().strip())
        if not name_dish:
            break
        list_ing = []
        for number in range(hm_dish):
          ingredient_name = f.readline().strip().split("|")
          list_ing.append({'ingredient_name': ingredient_name[0].strip(), 'quantity': ingredient_name[1].strip(), 'measure': ingredient_name[2].strip()})
          cook_book[name_dish] =  list_ing
        f.readline()

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingridients = {}
    for dis in dishes:
        if dis in cook_book.keys():
            for ing in cook_book[dis]:
                keys = ing.get('ingredient_name')
                count = {'measure': ing.get('measure'), 'quantity': int(ing.get('quantity'))*person_count}
                if keys not in ingridients.keys():
                    ingridients[keys] = count
                else:
                    new_count = {'measure': count.get('measure'), 'quantity': int(count.get('quantity')) * person_count}
                    ingridients[keys] = new_count
        else:
            print('нет такого рецепта')
    print(ingridients)

get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос', 'Омлет'], 2)