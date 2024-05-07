import configparser

def config():
    settings = configparser.ConfigParser()
    settings.read('database.ini')
    database = {'host': settings['DEFAULT']['host'],
                'database': settings['DEFAULT']['database'],
                'user': settings['DEFAULT']['user'],
                'password': settings['DEFAULT']['password']
                }
    return database




