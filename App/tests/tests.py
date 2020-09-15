import uuid

from django.test import TestCase
from fluentcheck import Is

from App.entities import Scheduler


class SchedulerTestCase(TestCase):
    @staticmethod
    def test_can_add_todo_list():
        """Scheduler can create empty"""
        scheduler = Scheduler()
        new_id = uuid.uuid4()

        scheduler.add_todo_list(new_id, "my todo list")

        Is(scheduler.get_amount_of_todo_lists()).not_none.integer.has_same_truth_of(1)

    @staticmethod
    def test_can_delete_some_list():
        scheduler = Scheduler()
        new_id = uuid.uuid4()

        scheduler.add_todo_list(new_id, "my todo list")
        scheduler.delete_todo_list(new_id)

        Is(scheduler.get_amount_of_todo_lists()).integer.zero

    @staticmethod
    def test_can_add_task():
        scheduler = Scheduler()
        todo_list_id = uuid.uuid4()
        task_id = uuid.uuid4()

        scheduler.add_todo_list(todo_list_id, "my todo list")

        scheduler.add_task(todo_list_id, task_id, "my new task")

        Is(scheduler.get_amount_of_tasks()).integer.between(1, 1)
