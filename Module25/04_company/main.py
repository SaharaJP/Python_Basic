from persons import Manager, Agent, Worker

employee_list = [
    Manager('Tom', 'Smith', 24), Manager('Tom', 'Smith', 24), Manager('Tom', 'Smith', 24),
    Agent('Tim', 'Martin', 31, 5000), Agent('Tim', 'Martin', 31, 5000), Agent('Tim', 'Martin', 31, 5000),
    Worker('Sam', 'Nate', 28, 40), Worker('Sam', 'Nate', 28, 40), Worker('Sam', 'Nate', 28, 40)
]

for employees in employee_list:
    print(employees.salary(), 'рублей', end = '\n\n')