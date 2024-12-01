import json
import os
import pandas as pd
from datetime import datetime

#__________________________________________________________________________________________________________
# ну начнем с калькулятора
def calculator():
    try:
        expression = input("введи пример: ")
        result = eval(expression)
        print(f"ответ: {result}")
    except ZeroDivisionError:
        print("ошибка деление на ноль")
    except Exception as e:
        print(f"{e}")



def create_task():
    tasks = load_tasks()
    task_id = len(tasks) + 1
    title = input("заголовок задачи: ")
    description = input("описание задачи: ")
    priority = input("приоритет задачи: ")
    due_date = input("дедлайн задачи: ")
    task = Task(task_id, title, description, False, priority, due_date)
    tasks.append(task)
    save_tasks(tasks)
    print("создано")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("пусто")
        return
    for task in tasks:
        print( f"{task.id}. {task.title} - {task.priority} - {task.due_date} - {'выполнено' if task.done else 'не выполнено'}"
        )


def create_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("заголовок заметки: ")
    content = input("содержимое заметки: ")
    note = Note(note_id, title, content)
    notes.append(note)
    save_notes(notes)
    print("создано")


def list_notes():
    notes = load_notes()
    if not notes:
        print("пусто")
        return
    for note in notes:
        print(f"{note.id}. {note.title} ({note.timestamp})")


def load_finance_records():
    try:
        with open(FINANCE_FILE, "r") as file:
            return [FinanceRecord.from_dict(record) for record in json.load(file)]
    except:
        return []


def save_finance_records(records):
    with open(FINANCE_FILE, "w") as file:
        json.dump([record.to_dict() for record in records], file, indent=4)


def create_finance_record():
    records = load_finance_records()
    record_id = len(records) + 1
    amount = float(input("сумма операции: "))
    category = input("категория операции: ")
    date = input("дата операции (ДД-ММ-ГГГГ): ")
    description = input("описание операции: ")
    record = FinanceRecord(record_id, amount, category, date, description)
    records.append(record)
    save_finance_records(records)
    print("создано")


def list_finance_records():
    records = load_finance_records()
    if not records:
        print("пусто")
        return
    for record in records:
        print(
            f"{record.id}. {record.amount} - {record.category} - {record.date} - {record.description}"
        )


def export_finance_records_to_csv():
    records = load_finance_records()
    df = pd.DataFrame([record.to_dict() for record in records])
    df.to_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\finance.csv", index=False)
    print("экспортировано")


def import_finance_records_from_csv():
    df = pd.read_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\finance.csv")
    records = [FinanceRecord.from_dict(row) for index, row in df.iterrows()]
    save_finance_records(records)
    print("импортировано")




def create_contact():
    contacts = load_contacts()
    contact_id = len(contacts) + 1
    name = input("имя : ")
    phone = input("номер : ")
    email = input("адрес электронной почты: ")
    contact = Contact(contact_id, name, phone, email)
    contacts.append(contact)
    save_contacts(contacts)
    print("создано")


def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("пусто")
        return
    for contact in contacts:
        print(f"{contact.id}. {contact.name} - {contact.phone} - {contact.email}")


def export_contacts_to_csv():
    contacts = load_contacts()
    df = pd.DataFrame([contact.to_dict() for contact in contacts])
    df.to_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\contacts.csv", index=False)
    print("эксплортировано")


def import_contacts_from_csv():
    df = pd.read_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\contacts.csv")
    contacts = [Contact.from_dict(row) for index, row in df.iterrows()]
    save_contacts(contacts)
    print("эксплортировано")

class Note:
    def __init__(self, id, title, content, timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def from_dict(data):
        return Note(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            timestamp=data["timestamp"],
        )


class Task:
    def __init__(
        self, id, title, description, done=False, priority="", due_date=None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            done=data["done"],
            priority=data["priority"],
            due_date=data["due_date"],
        )


class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }



    @staticmethod
    def from_dict(data):
        return Contact(
            id=data["id"], name=data["name"], phone=data["phone"], email=data["email"]
        )


class FinanceRecord:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description



    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }





    @staticmethod
    def from_dict(data):
        return FinanceRecord(
            id=data["id"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data["description"],
        )
# Загрузки файлов и выгрузки файлов все в одном месте
#______________________________________________________
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return [Contact.from_dict(contact) for contact in json.load(file)]
    except:
        return []



def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)




def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [Task.from_dict(task) for task in json.load(file)]
    except:
        return []

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return [Note.from_dict(note) for note in json.load(file)]
    except:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump([note.to_dict() for note in notes], file, indent=4)

def export_notes_to_csv():
    notes = load_notes()
    df = pd.DataFrame([note.to_dict() for note in notes])
    df.to_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\notes.csv", index=False)
    print("экспортировано")


def import_notes_from_csv():
    df = pd.read_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\notes.csv")
    notes = [Note.from_dict(row) for index, row in df.iterrows()]
    save_notes(notes)
    print("импортировано")

def export_tasks_to_csv():
    tasks = load_tasks()
    df = pd.DataFrame([task.to_dict() for task in tasks])
    df.to_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\tasks.csv", index=False)
    print("экспортировано")


def import_tasks_from_csv():
    df = pd.read_csv(r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\tasks.csv")
    tasks = [Task.from_dict(row) for index, row in df.iterrows()]
    save_tasks(tasks)
    print("импортировано")


class Manager:
    def main_menu(self):
        print("Добро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("действие: ")
        if choice == "1":
            self.manage_notes()
        elif choice == "2":
            self.manage_tasks()
        elif choice == "3":
            self.manage_contacts()
        elif choice == "4":
            self.manage_finances()
        elif choice == "5":
            self.calculator()
        elif choice == "6":
            sys.exit()
            exit()

    def manage_notes(self):
        print("Управление заметками")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Экспорт заметок в CSV")
        print("4. Импорт заметок из CSV")
        print("5. Назад")
        choice = input("действие: ")



        if choice == "1":
            create_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            export_notes_to_csv()
        elif choice == "4":
            import_notes_from_csv()
        elif choice == "5":
            self.main_menu()


    def manage_tasks(self):
        print("Управление задачами")
        print("1. Создать задачу")
        print("2. Просмотреть задачи")
        print("3. Экспорт задач в CSV")
        print("4. Импорт задач из CSV")
        print("5. Назад")
        choice = input("действие: ")
        if choice == "1":
            create_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            export_tasks_to_csv()
        elif choice == "4":
            import_tasks_from_csv()
        elif choice == "5":
            self.main_menu()




    def manage_contacts(self):
        print("Управление контактами")
        print("1. Создать контакт")
        print("2. Просмотреть контакты")
        print("3. Экспорт контактов в CSV")
        print("4. Импорт контактов из CSV")
        print("5. Назад")
        choice = input("действие: ")
        if choice == "1":
            create_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            export_contacts_to_csv()
        elif choice == "4":
            import_contacts_from_csv()
        elif choice == "5":
            self.main_menu()








    def manage_finances(self):
        print("Управление финансовыми записями")
        print("1. Создать финансовую запись")
        print("2. Просмотреть финансовые записи")
        print("3. Экспорт финансовых записей в CSV")
        print("4. Импорт финансовых записей из CSV")
        print("5. Назад")
        choice = input("действие: ")
        if choice == "1":
            create_finance_record()
        elif choice == "2":
            list_finance_records()
        elif choice == "3":
            export_finance_records_to_csv()
        elif choice == "4":
            import_finance_records_from_csv()
        elif choice == "5":
            self.main_menu()
        else:
            print("Некорректный ввод. Попробуйте снова.")
            self.manage_finances()
    def calculator(self):
        calculator()
        self.main_menu()

NOTES_FILE = r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\notes.json"
TASKS_FILE = r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\tasks.json"
FINANCE_FILE = r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\finance.json"
CONTACTS_FILE = r"C:\Users\ivans\OneDrive\Рабочий стол\питон 11\storage\contacts.json"








def main():
    manager = Manager()
    manager.main_menu()



if __name__ == "__main__":
    main()
