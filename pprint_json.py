
import json


def load_data(filepath):
    return json.load(filepath)


def pretty_print_json(data):
    pprint_json = json.dumps(data, indent=4, sort_keys=True)
    return pprint_json


if __name__ == '__main__':
    try:
        filepath = input('Вседите путь и имя файла: ')
        with open(filepath, 'r') as file_:
            data = load_data(file_)

    except FileNotFoundError:
        print ('Нет такого файла или папки. Программа будет закрыта.')
        exit()
    pprint_json = pretty_print_json(data)
    print (pprint_json)
