import uuid


class Scheduler(object):

    def __init__(self):
        self._todo_lists = []

    def add_todo_list(self, todo_list_id: uuid, todo_list_name: str):
        todo_list = TodoList(todo_list_id, todo_list_name)
        self._todo_lists.append(todo_list)
        return self

    def get_amount_of_tasks(self) -> int:
        return sum(todo_list.get_amount_of_tasks() for todo_list in self._todo_lists)

    def get_amount_of_todo_lists(self) -> int:
        return sum(1 for v in self._todo_lists if not v.is_deleted)

    def delete_todo_list(self, todo_list_id):
        todo_list = next((x for x in self._todo_lists if x.id == todo_list_id and not x.is_deleted), None)
        if todo_list:
            todo_list.check_as_deleted()

    def add_task(self, todo_list_id, task_id, title):
        todo_list = next((x for x in self._todo_lists if x.id == todo_list_id), None)
        if todo_list:
            todo_list.add_task(task_id, title)

    def restore_todo_list(self, todo_list_id):
        todo_list = next((x for x in self._todo_lists if x.id == todo_list_id and x.is_deleted), None)
        if todo_list:
            todo_list.uncheck_as_deleted()


class TodoList(object):
    def __init__(self, todo_list_id: uuid, name: str):
        self._id = todo_list_id
        self._name = name
        self._tasks = []
        self._is_deleted = False

    @property
    def id(self) -> "uuid":
        return self._id

    @property
    def is_deleted(self) -> "bool":
        return self._is_deleted

    def uncheck_as_deleted(self):
        self._is_deleted = False

    def check_as_deleted(self):
        self._is_deleted = True

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
