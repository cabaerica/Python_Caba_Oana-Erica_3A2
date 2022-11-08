def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def print_arguments(function):
        def f(*args, **dicts):
            print(args, dicts)
            return function(*args, **dicts)
        return f
    
def function_a():
    print("a)\n")
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)
    print(x)
    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)
    print(x)

def multiply_output(function):
        def f(*args, **dicts):
            return 2*function(*args, **dicts)
        return f

def multiply_by_three(x):
        return x * 3
    
def function_b():
    print("\nb)\n")
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)
    print(x)

def augment_function(function, decorators):
        def f(*args, **dicts):
            result = function
            for decorator in decorators:
                result = decorator(result)
            return result(*args, **dicts)
        return f
    
def function_c():
    print("\nc)\n")
    decorated_function = augment_function(
        add_numbers, [print_arguments, multiply_output])
    x = decorated_function(3, 4)
    print(x)

def main():
    function_a()
    function_b()
    function_c()

main()