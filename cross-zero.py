playing_field = list(range(1,10))
def markup_playing_field(playing_field):
    print ("…" * 13)
    for i in range(3):
        print ("⁞", playing_field[0+i*3], "⁞", playing_field[1+i*3], "⁞", playing_field[2+i*3], "⁞")
        print ("…" * 13)
def enter(player_choice):
    valid = False
    while not valid:
        player_answer = input("В какую клетку воткнем " + player_choice+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("По ходу ты ввел не число.. Пробуй есчо")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(playing_field[player_answer-1]) not in "XO"):
                playing_field[player_answer-1] = player_choice
                valid = True
            else:
                print ("Чувак, клетка занята, выбери другую")
        else:
            print ("Жесть... Введи число от 1 до 9")
def check_win(playing_field):
    winning_position = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in winning_position:
        if playing_field[each[0]] == playing_field[each[1]] == playing_field[each[2]]:
            return playing_field[each[0]]
    return False
def over(playing_field):
    counter = 0
    win = False
    while not win:
        markup_playing_field(playing_field)
        if counter % 2 == 0:
            enter("X")
        else:
            enter("O")
        counter += 1
        if counter > 4:
            win = check_win(playing_field)
            if win:
                print ("Поздравляем!", win, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("У Вас ничья!")
            break
    markup_playing_field(playing_field)
over(playing_field)
