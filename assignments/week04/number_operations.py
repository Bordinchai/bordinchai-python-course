def number_operation():
    numbers = []
    even_numbers = []
    odd_numbers = []
    above_average = []
    sum = 0
    for i in range(10):
        i = float(input(f"Enter your number {i+1}: "))
        numbers.append(i)
        sum += i
    print(f"Original numbers: {numbers}")
    average = sum / 10
    for i in numbers:
        if i > average:
            above_average.append(i)
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    print(f"Even numbers : {even_numbers}")
    print(f"Odd numbers  : {odd_numbers}")
    print(f"Above_Average: {above_average}")
    print(f"Sum          : {sum}")
    print(f"Average      : {average}")
    print(f"Min          : {min(numbers)}")
    print(f"Max          : {max(numbers)}")
number_operation()