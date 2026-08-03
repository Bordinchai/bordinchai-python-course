def prices_six_item():
    prices_list = []
    for item in range(0,6):
        item = int(input(f"Item {item + 1}: "))
        if item < 0:
            while True:
                item = int(input("Enter prices of item again: "))
                if item >= 0: break
        prices_list.append(item)
    return prices_list

def get_budget():
    budget = int(input("Enter total budget: "))
    if budget < 0:
        while True:
            budget = int(input("Enter total budget again: "))
            if budget >= 0: break
    return budget

def calculate(prices_list, budget):
    Bought_item = []
    Current_total = 0
    for price in prices_list:
        Current_total += price
        if Current_total <= budget:
            Bought_item.append(price)
            print(f"Item {prices_list.index(price) + 1} = {price} -> buy")
            print(f"Current total = {Current_total}\n")
        else:
            Current_total -= price
            print(f"Item {prices_list.index(price) + 1} = {price} -> cannot buy")
            print(f"Current total = {Current_total}\n")

    return Bought_item, Current_total

def main():
    print("Enter prices of 6 item:")
    prices_list = prices_six_item()
    print("\n")
    budget = get_budget()
    print("\n")
    total = calculate(prices_list, budget)
    Bought_item = total[0]
    Current_total = total[1]
    print(f"Bought item: {Bought_item}")
    print(f"Total spent: {Current_total}")
    print(f"Remaining budget: {budget - Current_total}")

main()