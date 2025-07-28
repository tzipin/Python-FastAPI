# 1 - מיון בסדר יורד לפי אורך המילה
def sort_list(my_list):
    my_list.sort()
    my_list.sort(reverse=True, key=len)
    return my_list


l = ["tyu", 'gh', "yttrium", 'yt', 'i']


print(sort_list(l))


# 2 - רשימה שמחזירה מילון
def analyze_list(lst):
    my_set = set()
    max_lst = 0
    min_lst = 10000
    for i in lst:
        my_set.add(i)
        if i > max_lst:
            max_lst = i
        if i < min_lst:
            min_lst = i
    my_dic = {set: my_set,
              max: max_lst,
              min: min_lst}
    return my_dic


print(analyze_list([1, 2, 3, 3, 4, 2, 5]))


# 3 - עובדים ששכרם גבוה
def filter_dict(d, threshold):
    height_salary = []
    for name, salary in d:
        if salary > threshold:
            height_salary.insert(name)
    return height_salary


workers = {"tzipi": 10000,
           "Miri": 1500,
           "Nati": 100
           }
print(filter_dict(workers, 500))
