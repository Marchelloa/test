import random
from concurrent import futures
from time import perf_counter
from itertools import repeat

COLOR = ['red', 'blue', 'green', 'gray', 'white', 'black', 'pink', 'brown', 'yellow', 'violet', 'orange']
TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
COLOR_DICT = {key: val for val, key in enumerate(COLOR)} # словарь вида {clolor: number}
NUMFLOAT_RAND = [random.random() for i in range(11)] # список случайных значений от 0 до 1
TEN_RAND = [random.randint(0, 9) for i in range(10)] # список случайных значений от 0 до 9
NUM1000 = [random.randint(1, 1000) for i in range(11)] # список случайных значений от 0 до 1000
ALPHABET = [chr(i) for i in range(65, 123)] # спсисок алфавита от a-z и A-Z

cycles = 1000000 # количество циклов расчёта
repeats = 5 # количество повторов в цикле
WORKERS = None # количество ядер

def algo_1():
    '''
    Функция содержащая эмитацию математических расчётов.
    '''
    color = random.choice(COLOR)
    num_float = NUMFLOAT_RAND[COLOR_DICT[color]]
    num1000_rand = NUM1000[random.choice(TEN)]
    expression = num1000_rand * num_float ** random.choice(TEN) + sum((i for i in range(0, num1000_rand)))
    return expression

def if_else():
    '''
    Функция содержащая эмитацию логических операций.
    '''
    color = random.choice(COLOR)
    letter =  random.choice(ALPHABET)
    letter_sample = random.sample(ALPHABET, 20)
    num = random.choice(TEN_RAND)
    
    if random.choice(COLOR) == color:
        result = COLOR_DICT[color] ** num
    if random.choice(ALPHABET) in letter_sample:
        result = sum(ord(letter)* i for i in range(num)) 
    else:
        result = ord(random.choice(ALPHABET))/(num + 1) + TEN[num-1] 
    return result

def test_perf(func1, func2, repeat, cycles):
    '''
    Функция замера производительности.
    '''        
    t0_local = perf_counter()
    for c in range(cycles):
        for r in range(repeat):
            func1()
            func2()
    finish = perf_counter() - t0_local
    
    return finish

list_cycles = [cycles] * futures.ProcessPoolExecutor()._max_workers

def factory_func(cycles, repeat):
    '''Функция фабрика для использования многопроцессорности.'''
    if WORKERS:
        cycles //= WORKERS
    else:
        cycles //= futures.ProcessPoolExecutor()._max_workers
    return test_perf(algo_1, if_else, repeat, cycles)
    

def main(): 
    '''Реализация многопроцессорного диспетчера '''   
    
    if WORKERS:
        workers = WORKERS
    else:
        workers = None

    time_result = []
    t0 = perf_counter()
    
    with futures.ProcessPoolExecutor(workers) as executor:
        print(f'Calculation with {executor._max_workers} processes')
        for result in executor.map(factory_func, list_cycles, repeat(repeats)):
            time_result.append(result)
    
    finish = perf_counter() - t0
    print(f'Cycles - {cycles}')
    print(f'Repeat - {repeats}')
    print(f'Total time: {finish:.2f}s')
    print('\nTime spent by each core:')    
    print(time_result)
    
if __name__ == '__main__':
    main()
    
    
            
        
