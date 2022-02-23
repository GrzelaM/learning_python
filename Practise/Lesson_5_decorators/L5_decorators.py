import time

def how_long(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        x = func(*args, **kwargs)
        finish = time.time()
        time_sec = finish - start
        print(f'Funkcja: {func.__name__} wykonywała się - {time_sec}')
        return x

    return wrapper

a,b = 10, 15
x,y,z = 2, 4, 6
sleepX_1 = 5
sleepX_2 = 3

def sleep_X_seconds(sleepX):
    print(f"Czas opóźnienia ustawiony na", sleepX)
    time.sleep(sleepX)

@how_long
def sum_two_numbers(a, b, sleepX_1):
    print("SUMA dwóch liczb:", a+b)
    sleep_X_seconds(sleepX_1)

@how_long
def sum_three_numbers(x, y, z, sleepX_2):
    print("SUMA trzech liczb:", x+y+z)
    sleep_X_seconds(sleepX_2)

sum_two_numbers(a,b, sleepX_1)
sum_three_numbers(x,y,z, sleepX_2)
