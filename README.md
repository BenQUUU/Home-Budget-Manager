# Home Budget Manager

Home Budget Manager is a simple command-line tool using the sqlite3 database for managing your home budget. It allows you to track expenses, income, view statistics, and more.

## Installation
* Clone the repository: ``git clone https://github.com/BenQUUU/Home-Budget-Manager.git``
* Run the application: ``python main.py``

## Command-line Options
* `--list`: View the list of expenses.
* `--stats`: View budget statistics.
* `--add-income`: Add a new income entry.
* `--add-expense`: Add a new expense entry.
* `--delete`: Delete an expense or income entry.

For additional details, run `python main.py --help`.

## Usage
The Home Budget Manager provides the following functionalities:
* List Expenses: `python main.py --list`
* View Statistics: `python main.py --stats`
* Add Income: `python main.py --add-income --name "Salary" --category "Income" --date "2023-01-01" --value 1000.0`
* Add Expense: `python main.py --add-expense --name "Groceries" --category "Food" --date "2023-01-05" --value 50.0`
* Delete Item: `python main.py --delete --id 1`

