def square(numbers):
    print("[square]Number are", numbers, hex(id(numbers)))
    for i in range(0, len(numbers)):
        numbers[i]=numbers[i]*numbers[i]
    print(" [square]New Number are", numbers, hex(id(numbers)))

numbers = [10,20,30,40,50]
print("Number are",numbers,hex(id(numbers)))
square(numbers)
numbers[1]=223
print(" [Main]New Number are", numbers, hex(id(numbers)))