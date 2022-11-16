from enum import Enum
from typing import Optional


class Product(Enum):
    Espresso = 1
    Latte = 2
    Cappuccino = 3


class Ingredient(Enum):
    water = 1
    milk = 2
    coffee = 3


class Coin(Enum):
    penny = 1
    nickle = 2
    dime = 3
    quarter = 4


class MenuItem:
    cost: float
    ingredients: dict[Ingredient, int]

    def __init__(self, cost: float, ingredients: dict[Ingredient, int]) -> None:
        self.cost = cost
        self.ingredients = ingredients


COIN_VALUE = {
    Coin.penny: 1,
    Coin.nickle: 5,
    Coin.dime: 10,
    Coin.quarter: 25,
}

coins_storage = {
    Coin.penny: 13,
    Coin.nickle: 5,
    Coin.dime: 6,
    Coin.quarter: 7,
}

MENU: dict[Product, MenuItem] = {
    Product.Espresso: MenuItem(
        cost=1.5,
        ingredients={
            Ingredient.water: 50,
            Ingredient.coffee: 18, }),
    Product.Latte: MenuItem(
        cost=2.5,
        ingredients={
            Ingredient.water: 200,
            Ingredient.milk: 150,
            Ingredient.coffee: 24,
        }, ),
    Product.Cappuccino: MenuItem(
        cost=3.0,
        ingredients={
            Ingredient.water: 250,
            Ingredient.milk: 100,
            Ingredient.coffee: 24,
        })
}

resources: dict[Ingredient, int] = {
    Ingredient.water: 0,
    Ingredient.milk: 100,
    Ingredient.coffee: 100,
}


def let_user_select_product() -> Product:
    selected_product: Optional[Product] = None

    while selected_product is None:
        prompt_str: str = ''

        for product in Product:
            prompt_str += product.value.__str__()
            prompt_str += ': '
            prompt_str += product.name
            prompt_str += ' '

        selected_product_str: str = input(prompt_str)

        try:
            if selected_product_str == 'off':
                quit()

            selected_product_int: int = int(selected_product_str)
            selected_product = Product(selected_product_int)
        except ValueError:
            print(f'Value must be between 1 and {len(Product)}')
            continue

        return selected_product

    raise RuntimeError('should not happen')


def check_if_can_be_made(selected_product: Product) -> bool:
    ingredients: dict[Ingredient, int] = MENU[selected_product].ingredients
    has_enough = True

    for ingredient in ingredients:
        available = resources[ingredient]
        if available < ingredients[ingredient]:
            has_enough = False
            print(f'Not enough {ingredient.name}')

    return has_enough


def main() -> None:
    selected_product = let_user_select_product()
    print(f'You selected {selected_product.name}')

    if not check_if_can_be_made(selected_product):
        print('')


while True:
    main()
