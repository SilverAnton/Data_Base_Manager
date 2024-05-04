from hh_api import HeadHunterApi
from Data_Base_Table import DataBaseTable
from utils import work_with_json
from Data_Base_manager import DataBaseManager

employers_param = ('employer_id integer PRIMARY KEY, name varchar, url varchar, alternate_url varchar, vacancies_url '
                   'varchar, open_vacancies integer')
vacancies_param = ('vacancy_id integer PRIMARY KEY, vacancy_name varchar, salary_from integer, salary_to integer, '
                   'currency varchar(30), city varchar, url varchar, employer_id integer REFERENCES employers('
                   'employer_id), employer_name varchar, description varchar, responsibility varchar')


def main_foo():
    obj_db_table = DataBaseTable()
    obj_db_table.create_table('employers', employers_param)
    obj_db_table.create_table('vacancies', vacancies_param)
    employer_kw = input('Введите ключевое слово для выбора работодателей')
    obj_api = HeadHunterApi()
    obj_api.add_employers(employer_kw)
    obj_api.add_vacancy()
    obj_api.save_as_json_employers()
    obj_api.save_as_json_vacancies()
    employers = work_with_json('employers.json')
    vacancies = work_with_json('vacancies.json')
    obj_db_table.fill_to_table(employers)
    obj_db_table.fill_to_table(vacancies)
    while True:
        print('Выберете действие для работы с данными')
        select_action = input(
            '1 - получить список всех компаний и кол-во вакансий у каждой компании\n'
            '2 - получить список всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию\n'
            '3 - получить среднюю зарплату по вакансиям\n'
            '4 - получить список всех вакансий, у которых зарплата выше средней \n'
            '5 - получить список вакансий по ключевому слову в названии вакансии\n'
            'Выход - закончить\n'
        )
        print()
        obj_dbm = DataBaseManager()
        if select_action == '1':
            for items in obj_dbm.get_companies_and_vacancies_count():
                print(items)
        elif select_action == '2':
            for items in obj_dbm.get_all_vacancies():
                print(items)
        elif select_action == '3':
            print(obj_dbm.get_avg_salary())
        elif select_action == '4':
            for items in obj_dbm.get_vacancies_with_higher_salary():
                print(items)
        elif select_action == '5':
            for items in obj_dbm.get_vacancies_with_keyword(
                    input('Введите ключевое слово для поиска названия вакансий')):
                print(items)
        elif select_action == 'Выход':
            obj_db_table.drop_table('vacancies')
            obj_db_table.drop_table('employers')
            break


main_foo()
