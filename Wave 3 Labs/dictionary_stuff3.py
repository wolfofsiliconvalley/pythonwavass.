fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for i, n in basket_items.items():
    if i in fruits:
        fruit_count += n
    elif i not in fruits:
        not_fruit_count += n
print(f'fruit_count = {fruit_count}\nnot_fruit_count = {not_fruit_count}')