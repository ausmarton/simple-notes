def add(first_number,second_number):
    return first_number+second_number
def multiply(first_number,second_number):
    result = 0
    first_number_abs = abs(first_number)

    is_positive = first_number == first_number_abs
    while first_number_abs != 0:
        result = add(second_number,result)
        first_number_abs = first_number_abs - 1
    if is_positive:
        return result
    else:
        return  -result