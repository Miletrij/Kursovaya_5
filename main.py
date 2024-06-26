from utils.user_interaction import user_interaction, delete_database, create_database
from src.db_manager import DBManager
import json
from path_database_ini import FILE2

db_name = input("Введите название базы данных:\n")
create_database(db_name)
db_manager = DBManager(db_name)
# user_input = input("Введите название компаний через запятую для просмотра.\n"
#                    "Если вакансии не указаны, программа вернет 10 первых.\n").split(",")
with open(FILE2, encoding="utf-8") as file:
    employer_list = json.load(file)
user_interaction(employer_list, db_name)
print("Список компаний сохранен в базе данных\n")

try:
    while True:
        print("Выберите число от 1 до 5:\n"
              "1. Получить список всех компаний и количество вакансий у каждой компании;\n"
              "2. Получить список всех вакансий с указанием названия компании, названия вакансии, "
              "зарплаты и ссылки на вакансию;\n"
              "3. Получить среднюю зарплату по вакансиям;\n"
              "4. Получить список всех вакансий, у которых зарплата выше средней по текущим вакансиям ;\n"
              "5. Получить список всех вакансий, в названиях которых содержатся указанные пользователем слова")
        number_user = int(input().strip())
        if number_user == 1:
            db_manager.get_companies_and_vacancies_count()
        elif number_user == 2:
            db_manager.get_all_vacancies()
        elif number_user == 3:
            db_manager.get_avg_salary()
        elif number_user == 4:
            db_manager.get_vacancies_with_higher_salary()
        elif number_user == 5:
            word_user = input("Введите название вакансии\n")
            db_manager.get_vacancies_with_keyword(word_user)
        elif number_user != "1" or "2" or "3" or "4" or "5":
            exit_user = input("Неверные данные\n"
                              "Введите 'exit' для выхода или повторите ввод\n").strip()
            if exit_user == 'exit':
                break
            else:
                continue
        user_question = input("Желаете продолжить?\n"
                              "1 - да\n"
                              "2 - нет\n").strip()
        if user_question == "1":
            continue
        elif user_question == "2":
            break
finally:
    db_manager.conn.close()
    print("Удаление БД.\n")
    delete_database(db_name)
    print("All good!")
