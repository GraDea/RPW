import uuid


class Scheduler(object):

    def __init__(self):
        self._items = []

    def add_todo_list(self, todo_list_id: uuid, todo_list_name: str):
        todo_list = TodoList(todo_list_id, todo_list_name)
        self._items.append(todo_list)
        return self

    def get_amount_of_tasks(self) -> int:
        return sum(todo_list.get_amount_of_tasks() for todo_list in self._items)

    def get_amount_of_todo_lists(self) -> int:
        return len(self._items)

    def delete_todo_list(self, id):
        todo_list = next((x for x in self._items if x.id == id), None)
        if todo_list:
            self._items.remove(todo_list)

    def add_task(self, todo_list_id, task_id, title):
        todo_list = next((x for x in self._items if x.id == todo_list_id), None)
        if todo_list:
            todo_list.add_task(task_id, title)


class TodoList(object):
    def __init__(self, todo_list_id: uuid, name: str):
        self._id = todo_list_id
        self._name = name
        self._tasks = []

    @property
    def id(self):
        return self._id

    def add_task(self, task_id, title):
        task = Task(task_id, title)
        self._tasks.append(task)

    def get_amount_of_tasks(self):
        return len(self._tasks)


class Task(object):
    def __init__(self, task_id, name):
        self._id = task_id
        self._name = name
        self._blockers = []

    def add_blocker(self, task_id):
        self._blockers.append(task_id)
