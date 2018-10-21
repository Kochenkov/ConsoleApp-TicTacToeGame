import sys
import random

def begin():
    global n,p1,p2,p3,p4,p5,p6,p7,p8,p9,x1,x2,x3,x4,x5,x6,x7,x8,x9,per,win,i
    #условия заполнения ячейки
    p1 = True
    p2 = True
    p3 = True
    p4 = True
    p5 = True
    p6 = True
    p7 = True
    p8 = True
    p9 = True
    #содержание ячеек
    x1 = ' '
    x2 = ' '
    x3 = ' '
    x4 = ' '
    x5 = ' '
    x6 = ' '
    x7 = ' '
    x8 = ' '
    x9 = ' '
    
    win = True #условие работы цикла
    per  = 'X' #переменная x и o
    i = 0 #счет ходов

    print("""Здравствуй, жалкая белковая форма жизни!
Сразись с искуственным интеллектом в игре 'крестики-нолики'.
Для того что бы сделать ход, введи номер ячейки.
Нумерация идет слева направо и сверху вниз, от 1 до 9.""")
    print('-------------')
    print('|',1,'|',2,'|',3,'|')
    print('-------------')
    print('|',4,'|',5,'|',6,'|')
    print('-------------')
    print('|',7,'|',8,'|',9,'|')
    print('-------------')

def choice():
    global you, enemy, ch
    ch = input('Введите x или o для выбора стороны: ')
    if ch=='x' or ch=='X':
        print("Вы играете за 'X' ")
        you = 'X'
        enemy = 'O'
    elif ch=='o' or ch=='O' or ch==0:
        print("Вы играете за 'О' ")
        you = 'O'
        enemy = 'X'
    else:
        print('Вы ввели некорректные данные, повторите ввод: ')
        choice()
    
#функция вывода игрового поля    
def printXO():
    print('-------------')
    print('|',x1,'|',x2,'|',x3,'|')
    print('-------------')
    print('|',x4,'|',x5,'|',x6,'|')
    print('-------------')
    print('|',x7,'|',x8,'|',x9,'|')
    print('-------------')

#функция условий заполнения ячеек
def inputXO():
    global n,p1,p2,p3,p4,p5,p6,p7,p8,p9,x1,x2,x3,x4,x5,x6,x7,x8,x9,per,i,you,enemy
    if n ==1 and p1 ==True:
        p1 = False
        x1 = per
        printXO()       
    elif n ==2 and p2 ==True:
        p2 = False
        x2 = per
        printXO()
    elif n ==3 and p3 ==True:
        p3 = False
        x3 = per
        printXO()       
    elif n ==4 and p4 ==True:
        p4 = False
        x4 = per
        printXO()
    elif n ==5 and p5 ==True:
        p5 = False
        x5 = per
        printXO()       
    elif n ==6 and p6 ==True:
        p6 = False
        x6 = per
        printXO()
    elif n ==7 and p7 ==True:
        p7 = False
        x7 = per
        printXO()       
    elif n ==8 and p8 ==True:
        p8 = False
        x8 = per
        printXO()
    elif n ==9 and p9 ==True:
        p9 = False
        x9 = per
        printXO()
    else:
        if i%2==0 and you=='X':
            n = int(input('Вы ввели неверный номер. Повторите действие:  '))
        elif i%2!=0 and you=='O':
            n = int(input('Вы ввели неверный номер. Повторите действие:  '))
        else:
            II()
        inputXO()
        
    
#функция условий победы игрока
def winX():
    global win, you, enemy
    if x1==you and x2==you and x3==you:
        print('Поздравляю, вы победили!')
        win = False
    elif x4==you and x5==you and x6==you:
        print('Поздравляю, вы победили!')
        win = False
    elif x7==you and x8==you and x9==you:
        print('Поздравляю, вы победили!')
        win = False
    elif x1==you and x4==you and x7==you:
        print('Поздравляю, вы победили!')
        win = False
    elif x2==you and x5==you and x8==you:
        print('Поздравляю, вы победили!')
        win = False
    elif x3==you and x6==you and x9==you:
        print('Поздравляю, вы победили!')
        win = False
    elif x1==you and x5==you and x9==you:
        print('Поздравляю, вы победили!')
        win = False
    elif x3==you and x5==you and x7==you:
        print('Поздравляю, вы победили!')
        win = False
    else:
        return

#функция условий победы противника ИИ
def winO():
    global win
    if x1==enemy and x2==enemy  and x3==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    elif x4==enemy and x5==enemy and x6==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    elif x7==enemy and x8==enemy and x9==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    elif x1==enemy and x4==enemy and x7==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    elif x2==enemy and x5==enemy and x8==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    elif x3==enemy and x6==enemy and x9==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    elif x1==enemy and x5==enemy and x9==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    elif x3==enemy and x5==enemy and x7==enemy:
        print('Вы проиграли, машинный разум одержал победу!')
        win = False
    else:
        return

#функция подсчета ИИ
def II():
    global n,p1,p2,p3,p4,p5,p6,p7,p8,p9,x1,x2,x3,x4,x5,x6,x7,x8,x9,per,i,enemy,you
    # проверка победы
    if (p1!=p2 or p1!=p3 or p2!=p3) and ( (x1==enemy and x2==enemy) or (x2==enemy and x3==enemy) or (x1==enemy and x3==enemy) ):
        n = random.randint(1, 3)
    elif (p4!=p5 or p4!=p6 or p5!=p6) and ( (x4==enemy and x5==enemy) or (x4==enemy and x6==enemy) or (x5==enemy and x6==enemy) ):
        n = random.randint(4, 6)
    elif (p7!=p8 or p7!=p9 or p8!=p9) and ( (x7==enemy and x8==enemy) or (x8==enemy and x9==enemy) or (x7==enemy and x9==enemy) ):
        n = random.randint(7, 9)
        
    elif (p1!=p4 or p1!=p7 or p4!=p7) and ( (x1==enemy and x4==enemy) or (x1==enemy and x7==enemy) or (x7==enemy and x4==enemy) ):
        n = random.choice([1,4,7])
    elif (p2!=p5 or p2!=p8 or p5!=p8) and ( (x2==enemy and x5==enemy) or (x2==enemy and x8==enemy) or (x5==enemy and x8==enemy) ):
        n = random.choice([2,5,8])
    elif (p3!=p6 or p6!=p9 or p3!=p9) and ( (x3==enemy and x9==enemy) or (x3==enemy and x6==enemy) or (x6==enemy and x9==enemy) ):
        n = random.choice([3,6,9])

    elif (p1!=p5 or p1!=p9 or p5!=p9) and ( (x1==enemy and x5==enemy) or (x1==enemy and x9==enemy) or (x5==enemy and x9==enemy) ):
        n = random.choice([1,5,9])
    elif (p3!=p5 or p3!=p7 or p5!=p7) and ( (x3==enemy and x5==enemy) or (x3==enemy and x7==enemy) or (x7==enemy and x5==enemy) ):
        n = random.choice([3,5,7])
     # проверка поражения  
    elif (p1!=p2 or p1!=p3 or p2!=p3) and ( (x1==you and x2==you) or (x2==you and x3==you) or (x1==you and x3==you) ):
        n = random.randint(1, 3)
    elif (p4!=p5 or p4!=p6 or p5!=p6) and ( (x4==you and x5==you) or (x4==you and x6==you) or (x5==you and x6==you) ):
        n = random.randint(4, 6)
    elif (p7!=p8 or p7!=p9 or p8!=p9) and ( (x7==you and x8==you) or (x8==you and x9==you) or (x7==you and x9==you) ):
        n = random.randint(7, 9)
        
    elif (p1!=p4 or p1!=p7 or p4!=p7) and ( (x1==you and x4==you) or (x1==you and x7==you) or (x7==you and x4==you) ):
        n = random.choice([1,4,7])
    elif (p2!=p5 or p2!=p8 or p5!=p8) and ( (x2==you and x5==you) or (x2==you and x8==you) or (x5==you and x8==you) ):
        n = random.choice([2,5,8])
    elif (p3!=p6 or p6!=p9 or p3!=p9) and ( (x3==you and x9==you) or (x3==you and x6==you) or (x6==you and x9==you) ):
        n = random.choice([3,6,9])

    elif (p1!=p5 or p1!=p9 or p5!=p9) and ( (x1==you and x5==you) or (x1==you and x9==you) or (x5==you and x9==you) ):
        n = random.choice([1,5,9])
    elif (p3!=p5 or p3!=p7 or p5!=p7) and ( (x3==you and x5==you) or (x3==you and x7==you) or (x7==you and x5==you) ):
        n = random.choice([3,5,7])

    else:
        if p5==True and you=='X':
            n = 5
        elif p5==False and ( (p1==False and p9==False) or (p3==False and p7==False) ) and you=='X' and x5=='O':
            n = random.choice([2,4,6,8])
        elif p5==False and ( (p1==False and p9==False) or (p3==False and p7==False) ) and you=='X' and x5=='X':
            n = random.choice([1,3,7,9])
        elif p5==False and (p1==True or p2==True or p7==True or p9==True) and you=='X':
            n = random.choice([1,3,7,9])
            
        elif p5==True and (p1==False or p2==False or p3==False or p4==False or p6==False or p7==False or p8==False or p9==False) and you=='O':
            n = 5
        else:
            n = random.randint(1, 9)


  
#функция очередости хода
def whileXO():
    global win, n, per, i
    while win == True:
        if i==9:
            print("Ничья")
            win = False
            continueXO()
        elif i%2==0 and you=='X':
            per = 'X'
            n = int(input('Ваш ход. Введи номер ячейки:  '))
            inputXO()
            i = i+1
            
        elif i%2!=0 and you=='X':
            per = 'O'
            print('Ход компьютера:')
            II()
            inputXO()
            i = i+1
            
        elif i%2==0 and you=='O':
            per = 'X'
            print('Ход компьютера:')
            II()
            inputXO()
            i = i+1
            
        elif i%2!=0 and you=='O':
            per = 'O'
            n = int(input('Ваш ход. Введи номер ячейки:  '))
            inputXO()
            i = i+1
        winX()
        winO()
        
#функция запуска игры по новой
def continueXO():
    message = input("""Желаете сыграть ещё? Введите 'да' или 'yes' для продолжения,
либо просто нажмите 'Enter' для выхода из программы: """)
    if message == 'да' or message == 'yes':
        prog()
    else:
        sys.exit()


#начало потока выполнения программы
def prog():   
    begin()
    choice()
    whileXO()
    continueXO()

    
# запускаем программу
prog()
