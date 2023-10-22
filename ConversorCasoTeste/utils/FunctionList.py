import math

unary_operators = ['!']

binary_operators = ['==', '>', '<', '>=', '<=', '-in']

logical_operators = ['&', '|']


def inside(var, args):
    for element in args:
        if str(var) == str(element):
            return True
    return False


def is_equal(var_a, var_b):
    return var_a == var_b


def greater_than(var_a, var_b):
    var_a, var_b = castFloat(var_a, var_b)
    return var_a > var_b


def greater_equal(var_a, var_b):
    var_a, var_b = castFloat(var_a, var_b)
    return var_a >= var_b


def lesser_than(var_a, var_b):
    var_a, var_b = castFloat(var_a, var_b)
    return var_a < var_b


def lesser_equal(var_a, var_b):
    var_a, var_b = castFloat(var_a, var_b)
    return var_a <= var_b


def operation_and(func_a, func_b):
    return func_a and func_b


def operation_or(func_a, func_b):
    return func_a or func_b


def operation_not(func_a):
    return not func_a


def operation_error(var_a, var_b):
    raise Exception("Operation error")


def unary_operation(operation_selector, func):
    operation = {
        unary_operators[0]: operation_not
    }
    chosen_function = operation.get(operation_selector, operation_error)
    return chosen_function(func)


def binary_operation(operation_selector, var_a, var_b):
    operation = {
        binary_operators[0]: is_equal,
        binary_operators[1]: greater_than,
        binary_operators[2]: lesser_than,
        binary_operators[3]: greater_equal,
        binary_operators[4]: lesser_equal,
        binary_operators[5]: inside
    }
    chosen_function = operation.get(operation_selector, operation_error)
    return chosen_function(var_a, var_b)


def logical_operation(operation_selector, func_a, func_b):
    operation = {
        logical_operators[0]: operation_and,
        logical_operators[1]: operation_or,
    }
    chosen_function = operation.get(operation_selector, operation_error)
    return chosen_function(func_a, func_b)


def castFloat(var_a, var_b):
    if type(var_a) == str:
        var_a = float(var_a)
    if type(var_b) == list:
        var_b = float(var_b[0])
    return var_a, var_b



