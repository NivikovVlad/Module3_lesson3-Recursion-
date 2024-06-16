
def get_multiplied_digits(number):
  str_number = str(number)
  if len(str_number) < 2:
    first = number
    return first
  else:
    first = int(str_number[0])
    number = int(str_number[1:])
    sum = first * get_multiplied_digits(number)
  return sum   

def get_number():
  number = input("Введите число: ")
  if not number.isdigit():
    print('Это не число! Введите число!')
    number = get_number()
  return number

number = get_number()
print('Произведение чисел =', get_multiplied_digits(number))  
