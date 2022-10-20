import random
import time


print('Добро пожаловать в числовую угадайку')
time.sleep(1)
print('Немного расскажу об условии игры. А условие очень простое, нужно угадать число, которое сгенерирует генератор '
      'чисел')
time.sleep(1)


def is_valid():
    if number.isdigit():
        if 1 <= int(number) <= 100:
            return True
        else:
            return False
    else:
        return False


while True:
    print('Давай проверим, как ты понял условия. Введите любое число от 1 до 100')
    number = input()
    if is_valid():
        number = int(number)
        print('Молорик различаешь цифры от букв')
        time.sleep(1)
        print('Ну что, приступаем к игре?')
        break
    else:
        print('Ты походу читать не умеешь')
        time.sleep(1)
        print('Давай тогда введем  число 1')
        time.sleep(1)
        print('Пробуй заново')
        time.sleep(1)
        print('Нажми цифру "1"')
        number = input()
        while number != 0:
            if number in '1':
                print('Молодец')
                time.sleep(1)
                print('Неужели! не прошло и полгода))')
                break
            else:
                print('Ты издеваешься')
                time.sleep(1)
                print('Не беси меня! Введи цифру "1"')
                number = input()
                continue
        break


time.sleep(1)
print("Введите правую границу")
right_range = int(input())
time.sleep(1)
print('А теперь можете угадать число, которое сгенерировано')


def Comparing_numbers():
    total = 1
    num = random.randint(1, right_range)
    while True:
        numbers = input()
        if is_valid():
            numbers = int(numbers)
            if numbers == num:
                print('Вы угадали, с ', total, ' раза, поздравляем!')
                break
            elif numbers < num:
                total += 1
                print('Ваше число меньше загаданного, попробуйте еще')
                continue
            elif numbers > num:
                total += 1
                print('Ваше число больше загаданного, попробуйте еще')
                continue
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


Comparing_numbers()
while True:
    print("Хотите сыграть еще раз? (Да, Нет)")
    ans = input()
    if ans.lower() == "да":
        time.sleep(1)
        print('Новое число уже сгенерировано')
        Comparing_numbers()
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break
