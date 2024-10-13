cook_book = {}
ingredients = []
with open("file_read_1.txt", "r") as file:
    for i in file:
        dish_name = i.strip()
        ing_count = file.readline()
        count = int(ing_count)
        for h in range(count):
            recepie = file.readline().strip().split(" | ")
            ingredients.append(recepie)
            product, quantity, measure = recepie
            ingredients.append({"product": product, "quantity": quantity, "measure": measure})
        file.readline()
    cook_book[dish_name]=ingredients

def get_shop_list_by_dishes(dishes, person_count):
    for h in ingredients:
        if h == dishes:
            quantity = quantity*person_count
            print(dishes)
get_shop_list_by_dishes(["Запеченный картофель", "Омлет"],2)



