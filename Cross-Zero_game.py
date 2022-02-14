# Практическое задание - проект "Крестики-нолики".
# Выполнил: студент группы FPW-60 Ильин Максим, февраль 2022
def greet_and_rules():
    print("x" * 60)
    print("                   Добро пожаловать в игру\n"
          "                       КРЕСТИКИ-НОЛИКИ")
    print("x" * 60)
    print("             В игре принимают участие два игрока.\n"
          "         Каждый выбирает один из символов - X или 0.\n"
          "    Игроки по очереди занимают символами свободные ячейки\n"
          "   игрового поля. Чтобы сделать ход, введите через пробел\n"
          "  координату ячейки на игровом поле (например 0 1 или 1 1).")
    print("x" * 60)
    print("  Игра завершается победой игрока, который первым выстроит\n"
          "   выбранные символы по одной из вертикалей, горизонталей\n"
          "     или диагоналей игрового поля. Первым ходит игрок X.\n"
          "                        ЖЕЛАЕМ УДАЧИ!")
    print("x" * 60)

def game_field():
    print()
    num = "     0  1  2 "
    print(num)
    for i, row in enumerate(field):
        row_str = f"   {i} {'  '.join(row)}  "
        print(row_str)
    print()

def moves():
    while True:
        cords = input("   Ваш ход: ").split()

        if len(cords) != 2:
            print("   Введите 2 координаты! ")
            continue

        x, y = cords

        if not x.isdigit() or not y.isdigit():
            print("   Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("   Координаты вне диапазона! ")
            continue

        if field[x][y] != "-":
            print("   Клетка уже занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("\nИгра окончена! Выиграл игрок X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("\nИгра окончена! Выиграл игрок 0!!!")
            return True
    return False

greet_and_rules()
field = [['-'] * 3 for _ in range(3)]
count = 0
while True:
    game_field()
    count += 1
    if count % 2 == 1:
        print("   Ходит игрок X!")
    else:
        print("   Ходит игрок 0!")

    x, y = moves()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("   Ничья!")
        break

input()
