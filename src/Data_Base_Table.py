import psycopg2
import requests


class DataBaseTable:
    """Класс для работы с таблицами базы данных"""

    @staticmethod
    def create_table(table_name, params):
        """Метод подключается к Data Base и создает таблицы по выбранному имени и параметрам"""
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        try:
            with psycopg2.connect(**conn) as connect:
                with connect.cursor() as cursor:
                    cursor.execute(f"CREATE TABLE {table_name}({params})")
        except requests.exceptions.HTTPError:
            print('ОЙ')

    @staticmethod
    def fill_to_table(items_list):
        """Метод выбирает и заполняет таблицы по входным данным"""
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }

        with psycopg2.connect(**conn) as connect:
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

    @staticmethod
    def drop_table(table_name):
        """Метод очищает таблицы от данных по имени таблицы"""
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        with psycopg2.connect(**conn) as connect:
            with connect.cursor() as cursor:
                cursor.execute(f'DROP TABLE {table_name}')


employers_param = ('employer_id integer PRIMARY KEY, name varchar, url varchar, alternate_url varchar, vacancies_url '
                   'varchar, open_vacancies integer')
vacancies_param = ('vacancy_id integer PRIMARY KEY, vacancy_name varchar, salary_from integer, salary_to integer, '
                   'currency varchar(30), city varchar, url varchar, employer_id integer REFERENCES employers('
                   'employer_id), employer_name varchar, description varchar, responsibility varchar')
