class Bank:
    credit = True  # Свойство класса, одно для всех. В данном примере предположим, что все банки выдают кредит

    def __init__(self, title, number, profit):
        self.title = title  # название банка
        self.number = number  # кол-во сотрудников в банке
        self.profit = profit  # прибыль банка

    def characteristic(self, year):
        print(
            f'Банк "{self.title}" по итогам {year} года получил {self.profit} рублей чистой прибыли, а количество сотрудников составило {self.number}.')


class Open(Bank):

    def __init__(self, title, number, profit, rating, position):
        super().__init__(title, number, profit)
        self.rating = rating
        self.position = position

    def characteristic(self, year):
        print(
            f'Банк "{self.title}" по итогам {year} года получил {self.profit} рублей чистой прибыли, а количество сотрудников составило {self.number}.')
        if (self.rating == True):
            print(f'{self.title} занимает {self.position} место в топе банков России.\n')


print('Выберите банк из топ ведущих банков России:  \n 1. Открытие \n 2. ВТБ \n 3. Тинькофф \n 4. Сбербанк \n 5. Почта Банк')
comand = int(input())
match comand:
    case 1:
        bank1 = Open('Открытие', 1236, 52563251, True, 1)
        bank1.characteristic('2023')
        mortgage = 452145
    case 2:
        bank1 = Open('ВТБ', 852, 5632482, True, 2)
        bank1.characteristic('2023')
        mortgage = 856325
    case 3:
        bank1 = Open('Тинькофф', 563, 4871293, True, 3)
        bank1.characteristic('2023')
        mortgage = 156125
    case 4:
        bank1 = Open('Сбербанк', 423, 658742, True, 4)
        bank1.characteristic('2023')
        mortgage = 65523
    case 5:
        bank1 = Open('Почта Банк', 126, 142296, True, 5)
        bank1.characteristic('2023')
        mortgage = 156156
    case _:
        print('Пройдите опрос заново!')
        raise SystemExit(1)


class Human:
    def __init__(self):
        self.age = input('Введите свой возраст: ')
        self.name = input('Введите свое имя: ')

    def credit(self):
        budget = int(input('Введите свой бюджет: '))
        budget1 = budget - mortgage
        if (budget1 < 0):
            print(f'{self.name}, банк не одобрил оформление ипотеки. Так как у вас нет денег, чтобы оплатить первоначальный взнос.')
        else:
            print(f'{self.name}, банк одобрил оформление ипотеки. После уплаты первоначального взноса ваш остаток по счету составляет {budget1}.')

client1 = Human()
client1.credit()

print('\nВсе совпадения случайны)')
