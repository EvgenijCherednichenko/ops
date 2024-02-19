import json
from datetime import datetime


def returns_list_json(filename):
    """
    Возвращает список словаря из файла operations.json
    """
    with open(filename, encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def filters_operations(operations):
    """
    Находит операции по EXECUTED, сортирует
    их по дате и возвращает 5 последних операций.
    """
    ex_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(ex_operations, key=lambda operation: operation['date'], reverse=True)
    five_last_operations = sorted_operations[:5]
    return five_last_operations


def masks_sender(card_number):
    """
   Возвращает номер карты в виде: <7000 79** **** 6361>
    """
    if 'Счет' in card_number:
        masked_number = card_number[:5] + '**' + card_number[-4:]
        return masked_number
    elif 'Unknown' in card_number:
        return 'Unknown'
    else:
        masked_number = card_number[:-16] + card_number[-16:-12] + ' ' + \
                        card_number[-12:-10] + '** **** ' + card_number[-4:]
        return masked_number


def masks_recipient(account_number):
    """Возвращает замаскированные номера счетов получателя."""
    masked_number = account_number[:5] + '**' + account_number[-4:]
    return masked_number


def converts_date(date_str):
    """
    Преобразует дату в формат <дата.месяц.год>
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%d.%m.%Y")


def collects_information(operation):
    """
    Выводит информацию.
    Дата.
    Описание.
    Номер от/кому.
    Сумма.
    Вызов функций маскирующих номера счетов/карт.
    """
    date = converts_date(operation['date'][:10])

    description = operation['description']

    from_card = operation.get('from', 'Unknown')
    to_card = operation['to']

    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    masked_from = masks_sender(from_card)
    masked_to = masks_recipient(to_card)

    return f'{date} {description}\n{masked_from} -> {masked_to}\n{amount} {currency}\n'


def displays_information(five_last_operations):
    """
    Выводит 5 последних операций.
    """
    form_operation = [collects_information(operation) for operation in five_last_operations]
    return form_operation
