class Project:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = [tasks]


class Task:
    def __init__(self, name, status, team_member):
        self.name = name
        self.status = status
        self.team_member = team_member


class TeamMember:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = [tasks]


def add_task(p, task):
    p.tasks.append(task)


def update_status(task, status):
    task.status = status

def show_status(o):
    for t in o.tasks:
        print(f"{t.status}")


p = Project('aaa', Task('bbb', 'בהמתנה', TeamMember('Tzipi', 'bbb')))
print(p.name)
add_task(p, Task('ccc', 'בהמתנה', TeamMember('Miri', 'ccc')))
for t in p.tasks:
    print(t.name)
update_status(p.tasks[0], 'בביצוע')
for t in p.tasks:
    print(t.status)
show_status(p)
