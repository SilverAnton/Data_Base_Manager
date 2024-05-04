import psycopg2


class DataBaseManager:
    """Класс для работы с объектами базы данных"""
    @staticmethod
    def get_companies_and_vacancies_count():
        """Метод возвращает названия работодателей и количество свободных вакансий из базы данных"""
        result = []
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        with psycopg2.connect(**conn) as connect:
            with connect.cursor() as cursor:
                cursor.execute('SELECT name, open_vacancies FROM employers')
                result.append(cursor.fetchall())

        return result[0]

    @staticmethod
    def get_all_vacancies():
        """Метод возвращает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки
        на вакансию из базы данных.
        """
        result = []
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        with psycopg2.connect(**conn) as connect:
            with connect.cursor() as cursor:
                cursor.execute('SELECT employer_name, vacancy_name, salary_from, salary_to, '
                               'currency, url FROM vacancies')
                result.append(cursor.fetchall())

        return result[0]

    @staticmethod
    def get_avg_salary():
        """Метод возвращает среднюю зарплату среди вакансий из базы данных"""
        result = []
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        with psycopg2.connect(**conn) as connect:
            with connect.cursor() as cursor:
                cursor.execute('SELECT AVG(salary_to) as avg_salary '
                               'FROM vacancies')
                result.append(cursor.fetchall())

        return result[0]

    @staticmethod
    def get_vacancies_with_higher_salary():
        """Метод возвращает вакансии с зарплатой выше средней из базы данных"""
        result = []
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        with psycopg2.connect(**conn) as connect:
            with connect.cursor() as cursor:
                cursor.execute('SELECT * FROM vacancies WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies) ')
                result.append(cursor.fetchall())

        return result[0]

    @staticmethod
    def get_vacancies_with_keyword(keyword):
        """Метод возвращает вакансии по ключевому слову из базы данных"""
        result = []
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        with psycopg2.connect(**conn) as connect:
            with connect.cursor() as cursor:
                cursor.execute(f"SELECT * FROM vacancies WHERE vacancy_name LIKE \'%{keyword}%\'")
                result.append(cursor.fetchall())

        return result[0]
