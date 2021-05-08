'''
시작 시각 : 14:00
종료 시각 : 17:00
'''


class Cake:
    def __init__(self, name, price, ingredient):
        self.name = name
        self.price = price
        self.ingredient = ingredient


class Shop:

    def __init__(self):
        self.ingredient = {}
        self.product = {}

    def buy_ingredient(self, buy_dict):
        if len(self.ingredient) == 0:
            self.ingredient = buy_dict
        else:
            for ing, num in buy_dict.items():
                if ing not in self.ingredient:
                    self.ingredient[ing] = num
                else:
                    self.ingredient[ing] += num

    def current_ingredient(self):
        print("현재 보유한 재료는", end=" ")
        for key, value in self.ingredient.items():
            print(str(key) + "(" + str(value) + "개)", end=", ")
        print("입니다.")

    def make_cake(self, cake):
        lack_ing = {}
        count = 0

        for needed_ing, needed_num in cake.ingredient.items():
            if needed_ing in self.ingredient.keys():
                if(needed_num <= self.ingredient[needed_ing]):
                    count += 1
                else:
                    lack_ing[needed_ing] = needed_num - self.ingredient[needed_ing]

            else:
                lack_ing[needed_ing] = needed_num

        if count == len(cake.ingredient):
            for ing, num in cake.ingredient.items():
                self.ingredient[ing] -= cake.ingredient[ing]
                if self.ingredient[ing] == 0:
                    del self.ingredient[ing]

            if cake.name not in self.product:
                self.product[cake.name] = 1
            else:
                self.product[cake.name] += 1
            print(f"{cake.name} 1개 완성!")

        if count < len(cake.ingredient):
            for key, value in lack_ing.items():
                print(f"{key} 재료가 {value}개", end=" ")
            print("부족합니다.")

class Pos:
    def __init__(self, cake_shop):
        self.cake_shop = cake_shop
        self.money = 0

    def current_cakes(self):
        print("현재 재고는")
        for key, value in self.cake_shop.product.items():
            if value == 0:
                del cake_shop.product[key]
            print(f"{key}: {value}")

    def sell_cake(self, cakename):
        if cakename in cake_shop.product:
            cake_shop.product[cakename] -= 1
            print(f"{cakename} 판매 완료. 현재 남은 {cakename}의 개수는 {cake_shop.product[cakename]}개 입니다.")
            if cake_shop.product[cakename] == 0:
                del cake_shop.product[cakename]
        else:
            print(f"{cakename} 재고가 없습니다.")

    def print_current_money(self):
        print(f"현재 판매 금액은 총 {self.money}원 입니다.")


cheesecake = Cake("Cheese Cake", 6900, {'cheese': 2, 'egg': 2, 'butter': 2})
chococake = Cake("Chocolate Cake", 5900, {'chocolate': 2, 'egg': 2, 'butter': 2})
carrotcake = Cake("Carrot Cake", 5500, {'carrot': 2, 'walnut': 2, 'egg': 1, 'butter': 1})
creamcake = Cake("Fresh Cream Cake", 4500, {'cream': 3, 'egg': 1, 'butter': 1})
swpotatocake = Cake("Sweet Potato Cake", 6500, {'sweet potato': 3, 'egg': 2, 'butter': 1})

cake_shop = Shop()
cake_shop.buy_ingredient({'cheese': 5, 'carrot': 3, 'sweet potato': 3, 'egg': 10, 'butter': 10})
cake_shop.current_ingredient()
cake_shop.buy_ingredient({'chocolate': 3, 'walnut': 2, 'egg': 12, 'butter': 12})
cake_shop.current_ingredient()

print("\nMAKE CAKE")
cake_shop.make_cake(creamcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(chococake)
print(cake_shop.ingredient)
cake_shop.make_cake(swpotatocake)
print(cake_shop.ingredient)
cake_shop.current_ingredient()

pos = Pos(cake_shop)
print()
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Chocolate Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')

print()
pos.print_current_money()
