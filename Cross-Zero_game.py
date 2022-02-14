# Практическое задание - проект "Крестики-нолики".
# Выполнил: студент группы FPW-60 Ильин Максим.
def greet_and_rules():
    print("*" * 57)
    print('                Добро пожаловать в игру\n'
          '                    КРЕСТИКИ-НОЛИКИ')
    print("*" * 57)
    print(" Игроки выбирают себе один из символов - либо X либо 0.\n"
          " По очереди ставят их на свободные клетки игрового поля.")
    print("*" * 57)
    print("Игра завершается победой игрока, который первым выстроит\n"
          "   свои знаки по одной из вертикалей,горизонталей или\n"
          "  диагоналей игрового поля. Для хода введите координату,\n"
          "         соотвествующую области на игровом поле.\n"
          "                 Первым ходит игорок X.\n"
          "                      Желаем удачи!")
    print("*" * 57)

def show():
    print()
    print("    | 1 | 2 | 3 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i+1} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def moves():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not x.isdigit() or not y.isdigit():
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)),
                ((1, 3), (2, 2), (3, 1)), ((1, 1), (2, 2), (3, 3)), ((1, 1), (2, 1), (3, 1)),
                ((1, 2), (2, 2), (3, 2)), ((1, 3), (2, 3), (3, 3)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[1]][c[2]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

greet_and_rules()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = moves()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break

