def basic_operations(x, y):
    result = {
        'Sum: ': x + y,
        'Differnce': x - y,
        'Product': x * y
    }
    try:
        result["Division"] = x / y
    except ZeroDivisionError:
        result["Division"] = "Error: Division by zero is not allowed"
    return result
    



def power_operations(base,exponent,**kwargs):
    result = pow(base,exponent)
    if 'modulo' in kwargs:
        try:
            result %= kwargs['modulo']
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"
    return result
 
 

