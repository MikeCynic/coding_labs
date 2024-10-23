numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
s = 0
for n in numbers:
    try:
        s += n
    except TypeError:
        continue
average = s / len(numbers)
numbers[numbers.index(None)] = average
print("Измененный список:", numbers)
