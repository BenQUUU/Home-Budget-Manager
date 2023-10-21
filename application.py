from parser import Parser
from repository import Repository


class Application:
    def __init__(self, repository: Repository):
        parser = Parser()
        self.arguments = parser.parse_args()
        self.repository = repository

    def main(self):
        match self.arguments.action:
            case 'list': self.list()
            case 'stats': self.stats()
            case 'delete': self.delete(self.arguments.id)
            case 'add_income': self.add_income(
                self.arguments.name,
                self.arguments.category,
                self.arguments.date,
                self.arguments.value
            )
            case 'add_expense': self.add_expense(
                self.arguments.name,
                self.arguments.category,
                self.arguments.date,
                self.arguments.value
            )

    def list(self):
        print('Expense list')

    def stats(self):
        print('Statistics')

    def delete(self, id:int):
        print('Delete')

    def add_income(self, name, category, date, value):
        print('Add income')
        self.repository.add_item(name, category, date, value)

    def add_expense(self, name, category, date, value):
        print('Add expense')
        self.repository.add_item(name, category, date, value * - 1)