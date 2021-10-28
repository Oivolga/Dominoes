import random


def gameplay(stock, comp, user, snake):
    line = ''
    print(70 * "=")
    print("Stock size:", len(stock))
    print("Computer pieces:", len(comp), "\n")
    if len(snake) > 6:
        print(f"{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}")
    else:
        for x in range(0, len(snake)):
            line += f"{snake[x]}"
        print(line)
    print("\nYour pieces:")
    for i in range(0, len(user)):
        print(f"{i + 1}: {user[i]}")


domino = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0], [5, 6], [4, 6], [3, 6], [4, 5], [2, 6], [3, 5],
          [1, 6], [2, 5], [3, 4], [0, 6], [1, 5], [2, 4], [0, 5], [1, 4], [2, 3], [0, 4], [1, 3], [0, 3], [1, 2],
          [0, 1], [0, 2]]
stock = domino.copy()
comp = []
user = []
start = []
snake = []
status = ''
finish = True
for x in range(7):
    comp.append(random.choice(stock))
    stock.remove(comp[len(comp) - 1])
    user.append(random.choice(stock))
    stock.remove(user[len(user) - 1])

for y in domino:
    if y in comp or y in user:
        start = y
        snake.append(start)
        break

comp.remove(start) if start in comp else user.remove(start)
msg1 = "It's your turn to make a move. Enter your command."
msg2 = "Computer is about to make a move. Press Enter to continue..."
go_user = True if len(comp) == 6 else False

while finish:
    if len(user) == 0:
        gameplay(stock, comp, user, snake)
        print("\nStatus: The game is over. You won!")
        break
    elif len(comp) == 0:
        gameplay(stock, comp, user, snake)
        print("\nStatus: The game is over. The computer won!")
        break
    elif not finish:
        print("\nStatus: The game is over. It's a draw!")
        break
    else:
        gameplay(stock, comp, user, snake)
        print("\nStatus:", msg1 if go_user else msg2)
        if go_user:
            while True:
                ch = input()
                try:
                    if int(ch) not in range(-len(user) - 1, len(user) + 1):
                        print("Invalid input. Please try again.")
                except ValueError:
                    print("Invalid input. Please try again.")
                if ch == "":
                    continue
                if int(ch) > 0 and int(ch) in range(-len(user) - 1, len(user) + 1) and snake[-1][-1] not in user[
                    int(ch) - 1]:
                    print("Illegal move. Please try again.")
                else:
                    break
            if int(ch) == 0:
                if len(stock) != 0:
                    user.append(random.choice(stock))
                    stock.remove(user[-1])
                else:
                    finish = False
                    print("\nStatus: The game is over. It's a draw!")
                    break
                go_user = False
            else:
                if int(ch) > 0 and int(ch) in range(-len(user) - 1, len(user) + 1):
                    if snake[-1][-1] != user[int(ch) - 1][0]:
                        user[int(ch) - 1].reverse()
                    snake.append(user[int(ch) - 1])
                    user.remove(user[int(ch) - 1])
                    go_user = False
                elif int(ch) < 0 and int(ch) in range(-len(user) - 1, len(user) + 1):
                    if snake[0][0] != user[-int(ch) - 1][1]:
                        user[-int(ch) - 1].reverse()
                    snake.insert(0, user[-int(ch) - 1])
                    user.remove(user[-int(ch) - 1])
                    go_user = False
        else:
            if input() == "":
                line1 = comp + snake
                line2 = []
                ball = {}
                score1 = []
                score2 = []
                for i in range(len(line1)):
                    for j in range(2):
                        line2.append(line1[i][j])
                for x in line2:
                    ball[x] = line2.count(x)
                for x in range(len(comp)):
                    score1.append((ball[comp[x][0]] + ball[comp[x][1]]))
                    score2.append(comp[x])
                line3 = list(zip(score1, score2))
                line3.sort(reverse=True)
                for i in range(0, len(line3)):
                    if snake[0][0] in line3[i][1]:
                        if snake[0][0] == line3[i][1][1]:
                            snake.insert(0, (line3[i][1]))
                            comp.remove(line3[i][1])
                            break
                        else:
                            line3[i][1].reverse()
                            snake.insert(0, (line3[i][1]))
                            comp.remove(line3[i][1])
                            break
                    elif snake[-1][-1] in line3[i][1]:
                        if snake[0][0] == line3[i][1][1]:
                            snake.append(line3[i][1])
                            comp.remove(line3[i][1])
                            break
                        else:
                            line3[i][1].reverse()
                            snake.append(line3[i][1])
                            comp.remove(line3[i][1])
                            break
                    else:
                        if len(stock) != 0:
                            comp.append(random.choice(stock))
                            stock.remove(comp[-1])
                            break
                        else:
                            finish = False
                            print("\nStatus: The game is over. It's a draw!")
                            break
                go_user = True
