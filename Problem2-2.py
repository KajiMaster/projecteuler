def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y,x+y
       
def even(seq):
    for number in seq:
        if not number % 2:
            yield number

def max_value(seq):
    for number in seq:
        if number < 4000000:
            yield number
        else:
            break

print sum(even(max_value(fib())))
