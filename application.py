from parser import Parser


class Application:
    def __init__(self):
        parser = Parser()
        self.arguments = parser.parse_args()

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

    def add_expense(self, name, category, date, value):
        print('Add expense')