import ast


def len_func(file):
    with open(file, "r", encoding="utf-8") as current_file:
        node = ast.parse(current_file.read())
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        if function.end_lineno - function.lineno + 1 > 20:
            return False
    return True


def lenFile(file):
    with open(file, 'r', encoding='utf-8') as f:
        num_lines = sum(1 for _ in f)
    return num_lines <= 200


def is_docstring(file):
    with open(file, "r", encoding="utf-8") as current_file:
        node = ast.parse(current_file.read())
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        if not ast.get_docstring(function):
            return False
    return True


print(len_func(r"C:\ציפי לימודים\Hitel Tasks\Cli\sign-up-1\Cli\simple_cli\Json_Cli.py"))
print(is_docstring(r"C:\ציפי לימודים\Hitel Tasks\Cli\sign-up-1\Cli\simple_cli\Json_Cli.py"))
