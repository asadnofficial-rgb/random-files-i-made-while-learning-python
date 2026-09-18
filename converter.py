def calc():
    a = input('Enter any number(decimal point is ok.)').strip()
    b = input('enter secondary number(decimal point is ok.)').strip()
    sign = input('what operation? type + for addition, - for subtraction, * for multiplication, / for division').strip()
    if sign == '+':
        return float(a) + float(b)
    elif sign == '-':
        return float(a) - float(b)
    elif sign == '*':
        return float(a)* float(b)
    elif sign == '/':
        return float(a)/float(b)
    else:
        print('Please enter a valid input')

final_value = calc()
print(final_value)

