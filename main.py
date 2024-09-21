from src.utils import get_transactions
from src.readers import read_transactions_csv, read_transactions_excel
from src.processing import filter_by_state


def main():
    """Пользователь выбирает из какого файла будет взята информация"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. \nВыберите необходимый файл:'
            '1. Получить информацию о транзакциях из JSON-файла'
            '2. Получить информацию о транзакциях из CSV-файла'
            '3. Получить информацию о транзакциях из XLSX-файла')
    user_choice = input()
    user_file = []
    while user_choice != ['1', '2', '3']:
        print('Некоректный выбор, попробуйте ещё раз')
        user_choice = input()
    else:
        if user_choice == '1':
            print('Для обработки выбран JSON-файл')
            user_file = get_transactions('data/operations.json')
        elif user_choice == '2':
            print('Для обработки выбран CSV-файл')
            user_file = read_transactions_csv('/transactions.csv')
        elif user_choice == '3':
            print('Для обработки выбран XLSX-файл')
            user_file = read_transactions_excel('/transactions.xlsx')

    question_status = ('Введите статус, по которому необходимо выполнить фильтрацию. \n'
                       'Доступные для фильтровки статусы:\n'
                       'EXECUTED, CANCELED, PENDING')

    user_status = input(f'{question_status}\n').upper()
    while user_status != ['EXECUTED, CANCELED, PENDING']:
        print(f'Статус операции "{user_status}" недоступен.\n')
        user_status = input(f'{user_status}').upper()
    else:
        print(f'Операция отфильтрована по статусу "{user_status}"')
        filter_status = filter_by_state(user_file, user_choice)
    return filter_status
