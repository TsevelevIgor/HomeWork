from src.utils import get_transactions
from src.readers import read_transactions_csv, read_transactions_excel
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency
from src.filters import filtered_operations


def main():
    """Пользователь выбирает из какого файла будет взята информация"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. \nВыберите необходимый пункт меню:'
          '\n1. Получить информацию о транзакциях из JSON-файла'
          '\n2. Получить информацию о транзакциях из CSV-файла'
          '\n3. Получить информацию о транзакциях из XLSX-файла')
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

    filtered_transactions = filter_by_state(user_file, user_status)

    date_sort = input('Отсортировать операции по дате? Да/Нет').lower()
    if date_sort == 'да':
        if input('Отсортировать по возрастанию или по убыванию?').lower() == 'по возрастанию':
            flag = False
        else:
            flag = True
        filtered_transactions = sort_by_date(filtered_transactions, flag)

    filter_by_rub = input("Выводить только рублевые транзакции? Да/Нет ")
    if filter_by_rub.lower() == "да":
        rub_transactions = filter_by_currency(filtered_transactions, "RUB")
        filtered_transactions = list(rub_transactions)[:-1]

    filter_by_word = input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
    if filter_by_word.lower() == "да":
        word = input("Введите слово: ")
        filtered_transactions = filtered_operations(filtered_transactions, word)

    print("Распечатываю итоговый список транзакций...")
    if len(filtered_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for tr in filtered_transactions:
            tr_date = get_date(tr["date"])
            currency = tr["operationAmount"]["currency"]["name"]
            if tr["description"] == "Открытие вклада":
                from_to = mask_account_card(tr["to"])
            else:
                from_to = mask_account_card(tr["from"]) + " -> " + mask_account_card(tr["to"])

            amount = tr["operationAmount"]["amount"]
            print(
                f"""{tr_date} {tr['description']}
    {from_to}
    Сумма: {round(float(amount))} {currency}
    """
            )
