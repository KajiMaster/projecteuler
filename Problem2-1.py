fibo_numbers = [1, 2]
for i in range(2, 35):
    this_one = (fibo_numbers[i-1]+fibo_numbers[i-2])
    if this_one < 4000000:
        fibo_numbers.append(this_one)

print fibo_numbers
