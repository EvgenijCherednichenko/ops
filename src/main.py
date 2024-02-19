from src import utils

filename = 'operations.json'
operations = utils.returns_list_json(filename)
last_five_operations = utils.filters_operations(operations)
formatted_operation = utils.displays_information(last_five_operations)
for operation in formatted_operation:
    print(operation)
