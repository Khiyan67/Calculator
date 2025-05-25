import math

# Create a dictionary of allowed math functions/constants
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith('__')}

print('📐 Calculator — type "exit" to quit')

while True:
    expr = input('>> ')
    if expr.lower() in ['exit', 'quit']:
        break
    try:
        # Evaluate the expression using only allowed math names
        result = eval(expr, {'__builtins__': None}, allowed_names)  
        print('= ', result)
    except Exception as e:
        print('Error:', e)              
