from pathlib import Path

from src import utils

BASE_DIR = Path(__file__).resolve().parent.parent
operations_path = BASE_DIR.joinpath('src', 'operations.json')


def test_last_operations(bank_fixture):
    assert len(utils.filters_operations(bank_fixture)) == 5


def test_mask_card_number(card_number, acct, unknown):
    assert utils.masks_sender(card_number) == "Maestro 1596 83** **** 5199"
    assert utils.masks_sender(acct) == "Счет **3493"
    assert utils.masks_sender(unknown) == "Unknown"


def test_mask_account_number(acct):
    assert utils.masks_recipient(acct) == "Счет **3493"


def test_format_date(data):
    assert utils.converts_date(data) == '26.08.2019'


def test_format_operation(money_transfer):
    formatted_operation = utils.collects_information(money_transfer)
    assert formatted_operation == '26.08.2019 Перевод организации\n' \
                                  'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
                                  '31957.58 руб.\n'


def test_format_recent_transactions(envelope):
    assert utils.displays_information(envelope) == ['08.12.2019 Открытие вклада\n'
                                                    'Unknown -> Счет **5907\n'
                                                    '41096.24 USD\n']
