import random
name = "Eldar"
age = 18
print(f"Привет, меня зовут {name} , мне 18 лет")
secret_number = random.randint(1, 20)
print("Эльдар, я загадал число")
count = 0
while True:
    quess = input("Какое число я загадал!")
    quess = int(quess)
    count += 1
    if quess < secret_number:
        print("Больше!")
    elif quess > secret_number:
        print("Меньше!")
    else:
        print(f"Ты победил! Количества попыток: {count}")
        break
