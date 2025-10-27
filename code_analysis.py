import ast
import os
from Graphs import *

UPLOAD_DIR = "uploads"
FILES_NAME = []
PROBLEMS_NAME = ["length of functions", "length of file", "there is docstring"]
PROBLEMS_IN_FILES = [0, 0, 0]
PROBLEMS_IN_FILE = []


def len_func(upload_file):
    cnt = 0
    len_funcs = []
    source = upload_file.file.read().decode("utf-8")
    upload_file.file.seek(0)
    node = ast.parse(source)
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        length = function.end_lineno - function.lineno + 1
        len_funcs.append(length)
        if length > 20:
            cnt += 1
    return cnt, len_funcs


def len_file(upload_file):
    source = upload_file.file.read().decode("utf-8")
    upload_file.file.seek(0)
    num_lines = len(source.splitlines())
    return num_lines <= 2


def is_docstring(upload_file):
    cnt = 0
    source = upload_file.file.read().decode("utf-8")
    upload_file.file.seek(0)
    node = ast.parse(source)
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        if not ast.get_docstring(function):
            cnt += 1
    return cnt


# def init(files: list[str]):
#   FILES_NAME.clear()
#   for file in files:
#       file_location = os.path.join(UPLOAD_DIR, file.filename)
#       with open(file_location, "wb") as buffer:
#          shutil.copyfileobj(file.file, buffer)
#     FILES_NAME.append(file.filename)
#    PROBLEMS_IN_FILE.clear()
#   PROBLEMS_IN_FILES[:] = [0, 0, 0]

def init(file_paths: list[str]):
    FILES_NAME.clear()
    PROBLEMS_IN_FILE.clear()
    PROBLEMS_IN_FILES[:] = [0, 0, 0]

    for path in file_paths:
        file_name = os.path.basename(path)
        FILES_NAME.append(file_name)


#def test(files: list[str]):
#    lengthes = []
 #   for file in files:
#        cnt_problems_in_file = 0
#        num_of_length_funcs, len_funcs = len_func(file)
#        lengthes += len_funcs
#        if num_of_length_funcs > 0:
#            PROBLEMS_IN_FILES[0] += 1
#            cnt_problems_in_file += 1
#        if not len_file(file):
#            PROBLEMS_IN_FILES[1] += 1
#            cnt_problems_in_file += 1
#        if is_docstring(file) > 0:
#            PROBLEMS_IN_FILES[2] += 1
#            cnt_problems_in_file += 1
#
#        PROBLEMS_IN_FILE.append(cnt_problems_in_file)
#    buffers = []
#    buffer1 = plot_pie_chart(PROBLEMS_NAME, PROBLEMS_IN_FILES)
#    buffers.append(buffer1)
#    buffer2 = plot_bar_chart(FILES_NAME, PROBLEMS_IN_FILE)
#    buffers.append(buffer2)
#    return buffers

def test(file_paths: list[str]):
    buffers = []

    for path in file_paths:
        file_name = os.path.basename(path)
        cnt_problems_in_file = 0

        num_length_funcs, _ = len_func(path)
        if num_length_funcs > 0:
            PROBLEMS_IN_FILES[0] += 1
            cnt_problems_in_file += 1

        if not len_file(path):
            PROBLEMS_IN_FILES[1] += 1
            cnt_problems_in_file += 1

        if is_docstring(path) > 0:
            PROBLEMS_IN_FILES[2] += 1
            cnt_problems_in_file += 1

        PROBLEMS_IN_FILE.append(cnt_problems_in_file)

    pie = plot_pie_chart(PROBLEMS_NAME, PROBLEMS_IN_FILES)
    bar = plot_bar_chart(FILES_NAME, PROBLEMS_IN_FILE)

    buffers.append(pie)
    buffers.append(bar)

    return buffers
