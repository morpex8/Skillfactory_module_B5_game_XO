pole = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]
def game_pole(pole):
    print("  0 1 2")
    for i in range(len(pole)):
        print(str(i), *pole[i])
def userInput(z):
    while True:
        vvod = input(f"Игрок {user} Введите кординаты: ").split()
        if len(vvod) != 2:
            print("Введите две координаты")
            continue
        if not(vvod[0].isdigit() and vvod[1].isdigit()):
            print("Введено не число")
            continue
        x, y = map(int, vvod)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Вышли из диапазона")
            continue
        if z[x][y] != "-":
            print("Ячейка занята")
            continue
        break
    return x, y
def winV1(x, user):
    def line_check(x1, x2, x3, user):
        if x1 == user and x2 == user and x3 == user:
            return True
    for i in range(3):
        if line_check(x[i][0], x[i][1], x[i][2], user) or \
        line_check(x[0][i], x[1][i], x[2][i], user) or \
        line_check(x[0][0], x[1][1], x[2][2], user) or \
        line_check(x[2][0], x[1][1], x[0][2], user):
            return True
    return False
counter = 1
while True:
    if counter % 2 == 1:
        user = "x"
    else:
        user = "o"
    game_pole(pole)
    x, y = userInput(pole)
    pole[x][y] = user
    if counter == 9:
        print(" Ходы кончились. Ничья")
        input("Нажмите любую клавишу для выхода.")
        break
    if winV1(pole, user):
        game_pole(pole)
        print("Выйграл игрок", user)
        input("Нажмите любую клавишу для выхода.")
        break
    counter += 1