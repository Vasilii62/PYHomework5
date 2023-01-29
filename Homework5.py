# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
# new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
# print(new_str)

# Задача 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать
# все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом"

# from random import randint

# def player_round(max_num, num, player):
#     take_sweet = -1
#     while 0 > take_sweet or take_sweet > max_num or take_sweet > num:
#         take_sweet = int(input(f'Сколько конфет из {num} возьмет игрок {player}? '))
#         if take_sweet > max_num:
#             print(f'Максимальное количество конфе, которые можно взять: {max_num}!')
#         elif take_sweet > num:
#             print(f'Осталось всего {num} конфет')
#         elif take_sweet == 0:
#             print(f'Необходимо взять минимум 1 конфету')
#         return take_sweet

# def bot_round(max_num, num):
#     if num <= max_num:
#         take_sweet = max_num
#     elif num > max_num and num - max_num <= max_num + 1:
#         take_sweet = num - max_num - 1
#     else:
#         take_sweet = num - (num // (max_num + 1)) * (max_num + 1) + 1
#     take_sweet = 1 if take_sweet == 0 or take_sweet > max_num else take_sweet
#     print(F'Бот берет {take_sweet} конфет(у).')
#     return take_sweet

# sweet = 2021
# max_sweet = 28
# print(f'На столе {sweet} конфет(а). Играют два игрока, делая ход друг за другом.\nПервый ход определяется жеребьевкой.\nЗа один ход можно забрать не более чем {max_sweet} конфет.\nВсе конфеты оппонента достаються сделавшему последний ход. Если хототе играть с ботом - введите имя "bot"')
# p_name = []
# p_name.append(input('Имя первого игрока: '))
# p_name.append(input('Имя второго игрока: '))

# in_game_player = randint(0, 1)
# print(f'Первым ходит игрок {p_name[in_game_player]}')

# game_sweet = sweet
# while game_sweet > 0:
#     if 'bot' not in p_name[in_game_player]:
#         game_sweet -= player_round(max_sweet, game_sweet, p_name[in_game_player])
#     else:
#         game_sweet -= bot_round(max_sweet, game_sweet)
#     print(f'Осталось конфет на столе: {game_sweet}')
#     in_game_player = int(not bool(in_game_player))
# print(f'Победил игрок {p_name[int(not bool(in_game_player))]}!')
    
# Задача 3. Создайте программу для игры в ""Крестики-нолики"".


# print(' Игра Крестики-нолики для двух игроков\n ')

# board = list(range(1,10))

# def draw_board(board):
#    print('_' * 13)
#    for i in range(3):
#       print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
#       print('_' * 13)

# def take_input(player_turn):
#    valid = False
#    while not valid:
#       print()
#       player_answer = input('Введите номер клетки для ' + player_turn +'? ')
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in 'XO'):
#             board[player_answer-1] = player_turn
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input('X')
#         else:
#            take_input('O')
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print()
#               print(tmp, 'выиграл!')
#               win = True
#               break
#         if counter == 9:
#             print('Ничья!')
#             break
#     draw_board(board)
#     print()
# main(board)

# input('Нажмите Enter для выхода!')

# Задача. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def rle_coding(data):
    count = 1
    res = ''
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            res = res + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data)-2] != data[-1]):
        res = res + str(count) + data[-1]
    return res


def rle_decoding(data):
    number = ''
    res = ''
    for i in range(len(data)):
        if not data[i].isalpha():
            number += data[i]
        else:
            res = res + data[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {rle_coding(s)}")
print(f"Текст после дешифровки: {rle_decoding(rle_coding(s))}")