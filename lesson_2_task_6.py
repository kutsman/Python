all_goods = []
key_1 = 'Название'
key_2 = 'Цена'
key_3 = 'Количество'
key_4 = 'Единицы'
n = abs(int(input('Напишите сколько товаров вы планируете ввести: ')))
i = 0
while True:
    i += 1
    if i <= n:
        val_1 = input(f"Введите название {i}-ого товара: ")
        val_2 = input(f"Введите цену {i}-ого товара: ")
        val_3 = input(f"Введите количество {i}-ого товара: ")
        val_4 = input(f"Введите единицы измерения {i}-ого товара: ")
        all_goods.append((i, {key_1: val_1, key_2: val_2, key_3: val_3, key_4: val_4}))
        # print(all_goods)
    good = {key_1: [], key_2: [], key_3: [], key_4: []}
    if i > n:
        i = 0
        while i <= n - 1:
            good[key_1].append(all_goods[i][1][key_1])
            good[key_2].append(all_goods[i][1][key_2])
            good[key_3].append(all_goods[i][1][key_3])
            good[key_4].append(all_goods[i][1][key_4])
            i += 1
        else:
            print(f"Аналитика о товарах: {good}")
            break
