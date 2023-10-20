import sys
import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Managing home budget')

        self.action_group = self.parser.add_mutually_exclusive_group(required=True)
        self.action_group.add_argument(
            '--add expense',
            dest='action',
            action='store_const',
            const='add_expense',
            help='Adding a new expense'
        )

        self.action_group.add_argument(
            '--add income',
            dest='action',
            action='store_const',
            const='add_income',
            help='Adding new income'
        )

        self.action_group.add_argument(
            '--delete',
            dest='action',
            action='store_const',
            const='delete',
            help='Deleting an expense or income'
        )

        self.action_group.add_argument(
            '--stats',
            dest='action',
            action='store_const',
            const='stats',
            help='View statistics'
        )

        self.action_group.add_argument(
            '--list',
            dest='action',
            action='store_const',
            const='list',
            help='View entries'
        )

        self.add_group = self.parser.add_argument_group('Adding an income or expense item')
        self.add_group.add_argument(
            '--name',
            type=str,
            help='Name of the element',
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )

        self.add_group.add_argument(
            '--date',
            type=str,
            help='Date of occurrence of the expense or income',
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )

        self.add_group.add_argument(
            '--value',
            type=float,
            help='Value',
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )

        self.delete_group = self.parser.add_argument_group('Deleting an item')
        self.delete_group.add_argument(
            '--id',
            type=int,
            help='The item ID',
            required='--delete' in sys.argv
        )

    def parse_args(self):
        return self.parser.parse_args()

