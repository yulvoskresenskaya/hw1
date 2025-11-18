ticket = int(input("Введите шестизначный номер билета: "))
digits = str(ticket)

if len(digits) == 6:
    sum_first = int(digits[0]) + int(digits[1]) + int(digits[2])
    sum_last = int(digits[3]) + int(digits[4]) + int(digits[5])
    if sum_first == sum_last:
        print("Счастливый билет!")
    else:
        print("Обычный билет")
