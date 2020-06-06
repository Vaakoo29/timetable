import pandas

class Table:

    def __init__(self, input_day, file):
        self.input_day = input_day.lower()
        self.file = pandas.read_csv(file)

    def day_info(self):

        if self.input_day == 'понедельник':
            df = self.file[['время', 'понедельник']]
            print(df)

        if self.input_day == 'вторник':
            df = self.file[['время', 'вторник']]
            print(df)
        
        if self.input_day == 'среда':
            df = self.file[['время', 'среда']]
            print(df)

        if self.input_day == 'четверг':
            df = self.file[['время', 'четверг']]
            print(df)

        if self.input_day == 'пятница':
            df = self.file[['время', 'пятница']]
            print(df)

        if self.input_day == 'суббота':
            df = self.file[['время', 'суббота']]
            print(df)

        if self.input_day == 'все':
            print(self.file.reset_index(drop=True))


class Day:

    def __init__(self, inp_d):
        self.inp_d = inp_d
        self.days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

    def validation(self):
        if isinstance(self.inp_d, str) == True:
            if self.inp_d in self.days:
                return True
            else:
                False
        else:
            return False

    def __str__(self):
        return f'{self.validation()}'