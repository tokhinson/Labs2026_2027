class Item:
    def __init__(self, letter, weight, value):
        self.letter = letter
        self.weight = weight
        self.value = value


def knapsack(items, capacity, bag):
    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        j = i        
        total_weight = weight
        node_value = value

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)

        return node_value

    def branch_bound(i, weight, value, bag):
        nonlocal max_value, best_bag
        if weight <= capacity and value > max_value:
            best_bag = bag.copy()
            max_value = value
        if i == len(items):
            return
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i+1, weight, value, bag.copy())
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            branch_bound(i+1, weight + items[i].weight, value + items[i].value, bag.copy() + [items[i]])


    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    best_bag = []
    max_value = 0
    branch_bound(0, 0, 0, bag)
    return max_value, best_bag

def inventory_print(inventory):
    letter_inventory = []
    for item in inventory:
        letter_inventory += item.letter * item.weight
    for i in range(3):
        if i != 1: 
            print(*letter_inventory[i*3:(i+1)*3])
        else:
            print(*letter_inventory[i*3:(i+1)*3][::-1])


if __name__ == "__main__":
    items = [
        Item("r", 3, 25), Item("p", 2, 15), Item("a", 2, 15), Item("m", 2, 20), 
        Item("i", 1, 5), Item("k", 1, 15), Item("x", 3, 20), Item("t", 1, 25), 
        Item("f", 1, 15), Item("d", 1, 10), Item("s", 2, 20), Item("c", 2, 20)
    ]
    bag = [items.pop(4)]
    capacity = 9 - bag[0].weight
    max_value, best_bag = knapsack(items, capacity, bag)
    real_value = 2 * max_value + 15 + bag[0].value - sum(item.value for item in items)

    if real_value < 0: print('Невозможно собрать неотрицательное кол-во очков')
    else:
        best_bag.sort(key=lambda x: x.weight, reverse=True)
        inventory_print(best_bag)
        print(f"Итоговые очки выживания: {real_value}")


    print("Все комбинации с положительным счётом:")
    total_value = sum(item.value for item in items)
    solutions = []
    for mask in range(1 << len(items)):
        taken = [items[i] for i in range(len(items)) if mask & (1 << i)]
        weight = sum(item.weight for item in taken) + bag[0].weight
        if weight > 9:
            continue
        score = 20 + 2 * sum(item.value for item in taken) - total_value
        if score > 0:
            solutions.append((score, taken + [bag[0]]))
    solutions.sort(key=lambda x: (-x[0], sorted(item.letter for item in x[1])))
    for score, taken in solutions:
        print(f"\n{score}:")
        inventory_print(sorted(taken, key=lambda x: x.weight, reverse=True))
    print(f"Всего комбинаций: {len(solutions)}")