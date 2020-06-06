from timetable import Day, Table

timetable_18704 = 'timetable.csv'

def answer_check(checking):
    if checking == '1' or checking == '2':
        return True
    else:
        return False


while True:


    print('Программа позволяет вывести расписание по дням.\nЕсть возможность вывести все расписание.')
    while True:

        response = input('1 - По дням, 2 - Вcе: ')
        if answer_check(response) == True:
            break
        else:
            print('Попробуйте еще раз!')

        

    if response == '1':

        while True:

            answer = input('Ввведите день недели: ')
            valid = Day(answer.lower())
            if valid.validation() == True:
                if answer.lower() == 'воскресенье':
                    print('Занятий нет. Выходной!')
                    continue
                else:
                    result = Table(answer.lower(), timetable_18704)
                    result.day_info()
                    break
            else:
                print('Попробуйте еще раз!')
                continue

        while True:

            continue_choice = input('1 - Продолжить, 2 - Выйти: ')

            if answer_check(continue_choice) == True:
                break
            else:
                print('Попробуйте еще раз!')
            
        if continue_choice == '1':
            continue
        elif continue_choice == '2':
            break  

    elif response == '2':

        result = Table('все', timetable_18704)
        result.day_info()

        while True:

            continue_choice = input('1 - Продолжить, 2 - Выйти: ')

            if answer_check(continue_choice) == True:
                break
            else:
                print('Попробуйте еще раз!')
            
        if continue_choice == '1':
            continue
        elif continue_choice == '2':
            break