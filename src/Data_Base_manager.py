import psycopg2
import requests


class DataBaseManager:
    """Класс для работы с объектами базы данных"""

    def __init__(self, config):
        try:
            self.connect = psycopg2.connect(**config)
        except requests.exceptions.HTTPError:
            print('ОЙ')

    def create_table(self, table_name, params):
        """Метод подключается к Data Base и создает таблицы по выбранному имени и параметрам"""
        connect = self.connect
        with connect.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {table_name}({params})")

    def fill_to_table(self, items_list):
        """Метод выбирает и заполняет таблицы по входным данным"""
        connect = self.connect
        with connect.cursor() as cursor:
            for item in items_list:
                if len(items_list) == 10:
                    query = 'INSERT INTO employers VALUES (%s, %s, %s, %s, %s, %s)'
                    cursor.execute(query, (item['employer_id'], item['name'],
                                           item['url'], item['alt_url'],
                                           item['vacancies_url'], item['open_vacancies']))
                else:
                    query_new = 'INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(query_new, (item['vacancy_id'], item['name'],
                                               item['salary_from'], item['salary_to'],
                                               item['currency'], item['city'],
                                               item['url'], item['employer_id'],
                                               item['employer_name'],
                                               item['requirement'], item['responsibility']))

    def drop_table(self, table_name):
        """Метод очищает таблицы от данных по имени таблицы"""
        connect = self.connect
        with connect.cursor() as cursor:
            cursor.execute(f'DROP TABLE {table_name}')

    def get_companies_and_vacancies_count(self):
        """Метод возвращает названия работодателей и количество свободных вакансий из базы данных"""
        connect = self.connect
        result = []
        with connect.cursor() as cursor:
            cursor.execute('SELECT name, open_vacancies FROM employers')
            result.append(cursor.fetchall())

        return result[0]

    def get_all_vacancies(self):
        """Метод возвращает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки
        на вакансию из базы данных.
        """
        connect = self.connect
        result = []
        with connect.cursor() as cursor:
            cursor.execute('SELECT employer_name, vacancy_name, salary_from, salary_to, '
                           'currency, url FROM vacancies')
            result.append(cursor.fetchall())

        return result[0]

    def get_avg_salary(self):
        """Метод возвращает среднюю зарплату среди вакансий из базы данных"""
        connect = self.connect
        result = []
        with connect.cursor() as cursor:
            cursor.execute('SELECT AVG(salary_to) as avg_salary '
                           'FROM vacancies')
            result.append(cursor.fetchall())

        return result[0]

    def get_vacancies_with_higher_salary(self):
        """Метод возвращает вакансии с зарплатой выше средней из базы данных"""
        connect = self.connect
        result = []
        with connect.cursor() as cursor:
            cursor.execute('SELECT * FROM vacancies WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies) ')
            result.append(cursor.fetchall())

        return result[0]

    def get_vacancies_with_keyword(self, keyword):
        """Метод возвращает вакансии по ключевому слову из базы данных"""
        connect = self.connect
        result = []
        with connect.cursor() as cursor:
            cursor.execute(f"SELECT * FROM vacancies WHERE vacancy_name LIKE \'%{keyword}%\'")
            result.append(cursor.fetchall())

        return result[0]
