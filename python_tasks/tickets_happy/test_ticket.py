from unittest import TestCase
from python_tasks.tickets_happy.tickets import Ticket


class TestTicket(TestCase):

    def test_create_ticket(self):
        instance_list = Ticket.tickets_create()
        tickets_list = [str(i).rjust(6, '0') for i in range(0, 999999)]
        self.assertEqual(len(tickets_list), len(instance_list))

    def test_moscow_ticket(self):
        count_ticket = 55252
        tickets_list = [str(i).rjust(6, '0') for i in range(0, 999999)]
        count_back = Ticket("path").moscow_count(tickets_list)
        self.assertEqual(count_ticket, count_back)

    def test_petersburg_ticket(self):
        count_ticket = 55252
        tickets_list = [str(i).rjust(6, '0') for i in range(0, 999999)]
        count_back = Ticket("path").petersburg_count(tickets_list)
        self.assertEqual(count_ticket, count_back)
