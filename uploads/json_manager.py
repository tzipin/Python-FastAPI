import json
import os.path
from itertools import islice

PATH = 'data.json'


def write_in_json(new_data):
    try:
        data = json.loads(new_data)
        if not os.path.exists(PATH):
            with open(PATH, 'w') as file:
                file.write('{}')
        with open(PATH, 'r+') as file:
            file_data = json.load(file)
            file_data.update(data)
            file.seek(0)
            json.dump(file_data, file)
    except Exception as e:
        raise e


def last_10_arguments():
    if not os.path.exists(PATH):
        raise Exception("file not exists")
    with open(PATH, 'r') as file:
        file_data = json.load(file)
        if file_data == {}:
            raise Exception("file empty")
        last_arguments = list(islice(reversed(file_data.items()), 10))
        return dict(last_arguments)

