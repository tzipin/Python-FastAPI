import ast
import json

DICT_PATH = 'dictionary.json'


def len_func(upload_file):
    source = upload_file.file.read().decode("utf-8")
    upload_file.file.seek(0)
    node = ast.parse(source)
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        if function.end_lineno - function.lineno + 1 > 20:
            return False
    return True


def len_file(upload_file):
    source = upload_file.file.read().decode("utf-8")
    upload_file.file.seek(0)
    num_lines = sum(1 for _ in source)
    return num_lines <= 200


def is_docstring(upload_file):
    source = upload_file.file.read().decode("utf-8")
    upload_file.file.seek(0)
    node = ast.parse(source)
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        if not ast.get_docstring(function):
            return False
    return True


def test(upload_file):
    problems_arr = [{"lenFunc": len_func(upload_file), "lenFile": len_file(upload_file), "MissingDocstring": is_docstring(upload_file)}]
    with open(DICT_PATH, "r", encoding="utf-8") as file:
        try:
            problems_dict = json.load(file)  # שימי לב - json.load, לא file.read()
        except json.JSONDecodeError:
            problems_dict = {}

    problems_dict[upload_file.filename] = problems_arr

    with open(DICT_PATH, "w", encoding="utf-8") as file:
        json.dump(problems_dict, file, ensure_ascii=False, indent=4)

    return problems_dict


# print(len_func(r"C:\ציפי לימודים\Hitel Tasks\Cli\sign-up-1\Cli\simple_cli\Json_Cli.py"))
# print(is_docstring(r"C:\ציפי לימודים\Hitel Tasks\Cli\sign-up-1\Cli\simple_cli\Json_Cli.py"))
