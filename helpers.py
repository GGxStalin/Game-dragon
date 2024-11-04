import random
import time
from data import *


def fight(current_enemy):
    round = random.randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player["hp"] > 0 and enemy_hp > 0:
        if round %2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}')
            crit = random.randint(1,100)
            if crit < player["luck"]:
                enemy_hp -= player["attack"]*3
            else:
                enemy_hp -= player["attack"]
            time.sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack'] * player["armor"]
            time.sleep(1)
        print(f'''{player['name']} - {player['hp']}, {enemy['name']} - {enemy_hp}''')
        print()
        time.sleep(1)
        round += 1


    if player["hp"] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player["hp"]=100
    return current_enemy


def training(training_type):
    skip = "2"
    if items["2"]["name"] in player["inventory"]:
        skip = input("Желаете пропустить тренировку? 1 - да, 2 - нет")
    if skip == "2":
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            time.sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= 0.09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()

def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')

def display_inventory():
    print("У вас есть:")
    for value in player["inventory"]:
        print(value)
    print(f'{player["money"]} монет')
    print()
    if "зелье удачи" in player["inventory"]:
        potion = input("Желаете выпить зелье удачи 1 - да, 2 - нет ")
        if potion == "1":
            player["luck"] += 7
            print(f'Готово теперь ваш шанс на крит. урон равен {player["luck"]}%')
            player["inventory"].remove("зелье удачи")
    if "Меч рыцаря" in player["inventory"]:
        sword = input("Желаете использовать меч рыцаря 1 - да, 2 - нет ")
        if sword == "1":
            player["attack"] += 15
            print(f'Готово теперь ваш урон равен {player["attack"]}')
            player["inventory"].remove("Меч рыцаря")
    if "Кольчуга" in player["inventory"]:
        armor = input("Желаете надеть кольчугу 1 - да, 2 - нет ")
        if armor == "1":
            player["armor"] -= 0.2
            print(f'Готово теперь броня поглощает {100 - player["armor"] * 100}% урона')
            player["inventory"].remove("Кольчуга")

def shop():
    print("Добро поджаловать путник, рад видеть тебя в своей лавке. Что желаешь приобрести?")
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')
    
    item = input("Введите название предмета: ")
    if item in player['inventory']:
        print(f'У тебя уже есть {items[item]["name"]}')
    elif player['money'] >= items[item]['price']:
        print(f'Ты успешно приобрёл {items[item]["name"]}')
        player['inventory'].append(items[item]["name"])
        player['money'] -= items[item]['price']
    else:
        print('Не хватает монет :(')
    print()
    print('Буду ждать тебя снова, путник!')
    print()

def earn():
    print("Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 650 монет. Соответственно, 33.33% чтобы их потерять")
    result = random.randint(1,100)
    time.sleep(1.5)
    print("результат...")
    time.sleep(1.5)
    print("страшно???")
    time.sleep(1.5)
    if result < 67:
        print("Поздравляю вы выиграли 650 монет")
        player["money"] += 650
    else:
        print("Повезет в следующий раз(")
        player["money"] -= 650
    print()
    print(f'Осталось монет {player["money"]}')
