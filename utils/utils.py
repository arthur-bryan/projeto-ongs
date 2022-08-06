from datetime import datetime


def obter_data_atual():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')
