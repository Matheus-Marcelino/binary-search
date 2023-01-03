from datetime import datetime

def time_func(func):
    def wrapper(*args, **kwargs):
        time_inicial = datetime.now()

        resultado = func(*args, **kwargs)

        time_final = datetime.now()

        time_total = time_final - time_inicial

        print(f'{func.__name__} demorou {time_total.total_seconds():.2f} segundos.')
        return resultado
    return wrapper
