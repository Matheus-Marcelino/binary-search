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


@time_func
def busca_binaria(vetor: tuple | list, pos_init: int, pos_final: int, x: int) -> int:
    """Busca otimizada em um vetor
        -> Funciona apenas para vetores organizados
        :vetor: Lista ou tupla
        :pos_init: Posição inicial do vetor
        :pos_final: Posição final do vetor
    """
    if pos_init <= pos_final:
        meio = (pos_init + pos_final) // 2

        if x > vetor[meio]:
            return busca_binaria(vetor, meio+1, pos_final, x)
        elif x < vetor[meio]:
            return busca_binaria(vetor, pos_init, meio-1, x)
        else:
            return meio

    return -1



@time_func
def procura_for(vetor: list, x: int) -> int:
    for c in vetor:
        if c == x:
            return c
